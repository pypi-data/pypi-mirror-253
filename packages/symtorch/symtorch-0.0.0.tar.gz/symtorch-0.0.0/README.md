<div align="center">
<img src="icon-with-text.svg" style="width: min(100%, 400px); height: auto;"/>
</div>

---

Fast, optimisable, symbolic expressions in PyTorch.

```python-repl
>>> from symtorch import symtorchify
>>> f = symtorchify("x**2 + 2.5*x + 1.7")
>>> f
x²+2.5x+1.7
>>> len(list(f.parameters()))
2
>>> import torch
>>> f.evalf({"x": torch.tensor(2.0)})
tensor([10.7000], grad_fn=<AddBackward0>)
```

## Installation

```bash
pip install symtorch
```

## Features and Documentation


## What about [SymPyTorch](https://github.com/patrick-kidger/sympytorch)?

This package attempts to supersede the amazing [Patrick Kidger]()'s original SymPyTorch.
Useful features improvements here are:

- implementations of `state_dict` and `load_state_dict` for all `SymTorch` objects, allowing for automated saving and loading via the native PyTorch mechanisms
- plays nicely with TorchScript, allowing for integration into C++ code
- a `SymbolAssignment` helper class to enable "drag-and-drop" replace of existing NN components with symbolic ones:
```python-repl
>>> model = nn.Sequential(
    SymbolAssignment(["a", "b"]), 
    symtorchify("3*a + b")
)
>>> model(torch.tensor([[1, 2], [3, 4]]))
tensor([[ 5.],
        [13.]], grad_fn=<AddBackward0>)
```
