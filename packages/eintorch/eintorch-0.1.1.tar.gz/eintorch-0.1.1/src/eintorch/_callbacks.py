import inspect
from inspect import signature
from typing import Any, Callable, Union

SINGLE_POSITIONALS = frozenset(
    (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
)


def count_positional_args(fun: Callable[..., Any]) -> Union[int, None]:
    sig = signature(fun)
    if not all(p.kind in SINGLE_POSITIONALS for p in sig.parameters.values()):
        return None
    return len(sig.parameters)
