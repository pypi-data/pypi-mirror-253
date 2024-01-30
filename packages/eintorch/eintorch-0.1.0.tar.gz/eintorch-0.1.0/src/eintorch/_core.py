from typing import TYPE_CHECKING, Any, Callable

import functorch.dim

from ._callbacks import count_positional_args

if TYPE_CHECKING:
    import torch


def array(fun: Callable[..., Any]) -> "torch.Tensor":
    k = count_positional_args(fun)
    if k is None:
        raise ValueError("Callback must only take positional arguments")
    if not k:
        raise ValueError("Callback must take at least one argument")
    indices = functorch.dim.dims(k)
    return fun(*indices).order(*indices)
