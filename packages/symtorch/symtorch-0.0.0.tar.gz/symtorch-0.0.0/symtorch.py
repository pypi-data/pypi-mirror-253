# TODO:
# - add custom function registration
# - elegant way to avoid this torch.repeat business
#    - perhaps move to symtorchify only returning Expressions?
#       need behaviour for wrapping Symbol and Parameter - subclasses?
# - profile for speed

from __future__ import annotations

from abc import ABC, abstractmethod
from functools import reduce, wraps
from typing import Callable, NamedTuple, TypeVar, cast, overload

import sympy
import torch
from torch import nn
from torch.nn.modules.module import _EXTRA_STATE_KEY_SUFFIX
from torch.types import Number

__version__ = "0.0.0"


T = TypeVar("T")


def _take_unlimited_args(two_arg_fn: Callable[[T, T], T]):
    """
    convert a function that takes two arguments
    into a function that takes an unlimited number
    and applies the two-argument function to them
    sequentially via reduce
    """

    @wraps(two_arg_fn)
    def wrapper(*args: T) -> T:
        return reduce(two_arg_fn, args)

    return wrapper


TorchOperation = Callable[..., torch.Tensor]
_sympy_torch_analogues: list[tuple[type[sympy.Expr], TorchOperation]] = [
    (sympy.Add, _take_unlimited_args(torch.add)),
    (sympy.Mul, _take_unlimited_args(torch.mul)),
    (sympy.Pow, torch.pow),
    (sympy.exp, torch.exp),
    (sympy.log, torch.log),
    (sympy.sin, torch.sin),
    (sympy.cos, torch.cos),
    (sympy.tan, torch.tan),
    (sympy.Abs, torch.abs),
    (sympy.Min, _take_unlimited_args(torch.min)),
    (sympy.Max, _take_unlimited_args(torch.max)),
    (sympy.Identity, lambda x: x),
]
_sympy_to_torch = dict(_sympy_torch_analogues)
_torch_to_sympy = {sympy: torch for torch, sympy in _sympy_torch_analogues}


def to_significant_figures(x: float | int, sf: int = 3) -> str:
    """
    Get a string representation of a float, rounded to
    `sf` significant figures.
    """

    # do the actual rounding
    possibly_scientific = f"{x:.{sf}g}"

    # this might be in e.g. 1.23e+02 format,
    # so convert to float and back to string
    return f"{float(possibly_scientific):g}"


class SymModule(nn.Module, ABC):
    """Base class for symbolic modules."""

    def forward(self, symbol_dict: dict[str, torch.Tensor]) -> torch.Tensor:
        return self.evalf(symbol_dict)

    @abstractmethod
    def evalf(self, symbol_dict: dict[str, torch.Tensor]) -> torch.Tensor:
        """Evaluate the expression via substitution."""

    @abstractmethod
    def sympy(self, sig_fig: int = 3) -> sympy.Basic:
        """
        Get an equivalent sympy expression, with numerical values
        rounded to `sig_fig` significant figures.
        """

    def _repr_latex_(self):
        return self.sympy()._repr_latex_()


class Symbol(SymModule):
    def __init__(self, symbol: str):
        super().__init__()
        self.symbol = symbol

    def evalf(self, symbol_dict: dict[str, torch.Tensor]) -> torch.Tensor:
        return symbol_dict[self.symbol]

    def __repr__(self):
        return self.symbol

    def sympy(self, sig_fig: int = 3) -> sympy.Basic:
        return sympy.Symbol(self.symbol)

    def get_extra_state(self) -> str:
        return self.symbol

    def set_extra_state(self, symbol: str) -> None:
        self.symbol = symbol


class Parameter(SymModule):
    def __init__(self, value: Number, trainable: bool = True):
        super().__init__()
        self.param = nn.Parameter(torch.tensor(value), trainable)

    def evalf(self, symbol_dict: dict[str, torch.Tensor]) -> torch.Tensor:
        # N_inputs = next(iter(symbol_dict.values())).shape[:-1]
        # return self.param.repeat(*N_inputs, 1)
        return self.param

    def __repr__(self):
        return to_significant_figures(self.param.item())

    def sympy(self, sig_fig: int = 3) -> sympy.Basic:
        if self.param.dtype == torch.int64:
            return sympy.Integer(self.param.item())
        return sympy.Float(to_significant_figures(self.param.item(), sig_fig))


class ExpressionState(NamedTuple):
    expression: str
    trainable: bool
    trainable_ints: bool


class Expression(SymModule):
    """
    A symbolic expression, implemented as a tree of torch operations,
    with `Symbol` and `Parameter` leaves.
    """

    def __init__(
        self,
        operation: TorchOperation,
        args: list[SymModule],
        trainable: bool = True,
        trainable_ints: bool = False,
    ):
        super().__init__()
        self.operation: TorchOperation = operation

        # explicitly not an nn.ModuleList:
        # Expressions should be thought of as a single Module - the fact that we
        # build a tree of such as our implementation should not effect this
        # hence we don't want to register these as submodules
        # so that loading/saving works nicely
        self.args = args

        self.trainable = trainable
        self.trainable_ints = trainable_ints

        _parameters = {}
        i = 0

        def _add_params(expr: Expression):
            nonlocal i

            for arg in expr.args:
                if isinstance(arg, Parameter) and arg.param.requires_grad:
                    _parameters[str(i)] = arg.param
                    i += 1
                elif isinstance(arg, Expression):
                    _add_params(arg)

        _add_params(self)
        self._parameters = _parameters

    def evalf(self, symbol_dict: dict[str, torch.Tensor]) -> torch.Tensor:
        return self.operation(*[arg.evalf(symbol_dict) for arg in self.args])

    def __repr__(self):
        sympy_name = _torch_to_sympy[self.operation].__name__
        return f"{sympy_name}({', '.join(map(repr, self.args))})"

    def sympy(self, sig_fig: int = 3) -> sympy.Basic:
        sympy_class = _torch_to_sympy[self.operation]
        return sympy_class(*[arg.sympy(sig_fig) for arg in self.args])

    def get_extra_state(self) -> ExpressionState:
        return ExpressionState(
            expression=repr(self.sympy(sig_fig=20)),
            trainable=self.trainable,
            trainable_ints=self.trainable_ints,
        )

    def set_extra_state(self, state: ExpressionState) -> None:
        expression, trainable, trainable_ints = state
        symtorch: Expression = symtorchify(
            expression, trainable=trainable, trainable_ints=trainable_ints
        )  # type: ignore
        self.operation = symtorch.operation
        self.args = symtorch.args

    def _save_to_state_dict(self, destination, prefix, keep_vars):
        # don't save the parameters!
        destination[prefix + _EXTRA_STATE_KEY_SUFFIX] = self.get_extra_state()

    def _load_from_state_dict(
        self,
        state_dict,
        prefix,
        local_metadata,
        strict,
        missing_keys,
        unexpected_keys,
        error_msgs,
    ):
        self.set_extra_state(state_dict[prefix + _EXTRA_STATE_KEY_SUFFIX])

    @property
    def free_symbols(self) -> set[str]:
        def _get_symbol(arg: SymModule) -> set[str]:
            if isinstance(arg, Symbol):
                return {arg.symbol}
            elif isinstance(arg, Expression):
                return arg.free_symbols
            else:
                return set()

        return reduce(set.union, map(_get_symbol, self.args), set())

    def forward(
        self, X: dict[str, torch.Tensor] | torch.Tensor
    ) -> torch.Tensor:
        if isinstance(X, torch.Tensor):
            free_symbols = self.free_symbols
            if len(free_symbols) == 0:
                return self.evalf({})
            if len(self.free_symbols) == 1:
                symbol = next(iter(free_symbols))
                return self.evalf({symbol: X})
            else:
                raise ValueError(
                    "Expression has more than one free symbol, "
                    "but only a single tensor was passed. "
                    "Pass a mapping of symbols to tensors instead, "
                    "or use a SymbolAssignment module to convert "
                    "a tensor into a mapping automatically."
                )

        return self.evalf(X)


def Placeholder() -> Expression:
    return Expression(_sympy_to_torch[sympy.Identity], [Symbol("x")])


@overload
def symtorchify(
    expr: Number, trainable: bool = True, trainable_ints: bool = False
) -> Parameter:
    ...


@overload
def symtorchify(
    expr: str, trainable: bool = True, trainable_ints: bool = False
) -> SymModule:
    ...


@overload
def symtorchify(
    expr: sympy.Symbol, trainable: bool = True, trainable_ints: bool = False
) -> Symbol:
    ...


@overload
def symtorchify(
    expr: sympy.Basic, trainable: bool = True, trainable_ints: bool = False
) -> SymModule:
    ...


def symtorchify(
    expr: str | sympy.Basic | Number,
    trainable: bool = True,
    trainable_ints: bool = False,
) -> SymModule:
    if trainable_ints and not trainable:
        raise ValueError("`trainable` must be True if `trainable_ints` is True")

    actual_expr = (
        sympy.sympify(expr) if not isinstance(expr, sympy.Basic) else expr
    )

    if isinstance(actual_expr, sympy.Symbol):
        return Symbol(str(actual_expr))

    if isinstance(actual_expr, (sympy.Number, sympy.NumberSymbol)):
        if actual_expr.is_integer and not trainable_ints:  # type: ignore
            return Parameter(int(actual_expr), trainable=False)
        else:
            return Parameter(float(actual_expr), trainable)

    actual_expr = cast(sympy.Expr, actual_expr)
    torch_op = _sympy_to_torch.get(actual_expr.__class__)
    if torch_op is None:
        raise ValueError(
            f"Expressions of type {actual_expr.__class__.__name__} are "
            "not (yet) supported"
        )

    args = [
        symtorchify(arg, trainable=trainable, trainable_ints=trainable_ints)
        for arg in actual_expr.args
    ]

    return Expression(
        torch_op,
        args,
        trainable=trainable,
        trainable_ints=trainable_ints,
    )


class SymbolAssignment(nn.Module):
    """
    Convert a tensor, `X`, of shape (..., N) into a dictionary
    of symbols, {s: X[..., [i]]}, where s is the i'th symbol in
    `symbol_order`.
    """

    def __init__(
        self,
        symbol_order: list[str] | None = None,
    ):
        super().__init__()
        self.symbol_order = symbol_order

    def forward(self, X: torch.Tensor):
        if self.symbol_order is None:
            raise ValueError(
                "SymbolAssignment must be given a symbol_order "
                "before it can be used"
            )
        symbol_dict = {s: X[..., [i]] for i, s in enumerate(self.symbol_order)}
        return symbol_dict

    def __repr__(self):
        return f"SymbolAssignment({self.symbol_order})"

    def get_extra_state(self) -> list[str] | None:
        return self.symbol_order

    def set_extra_state(self, symbol_order: list[str]) -> None:
        self.symbol_order = symbol_order
