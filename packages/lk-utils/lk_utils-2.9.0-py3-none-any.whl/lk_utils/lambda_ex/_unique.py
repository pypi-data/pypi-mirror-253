# DELETE this module.

import typing as t
from types import FunctionType


class T:
    DuplicateLocalsScheme = t.Literal['exclusive', 'ignore', 'override']
    FuncArgsNum = int  # the number of arguments. 0-3
    FuncId = str


class _Config:
    duplicate_locals_scheme: T.DuplicateLocalsScheme = 'override'
    use_thread_pool: bool = False


config = _Config()


def get_func_args_count(func: FunctionType) -> T.FuncArgsNum:
    cnt = func.__code__.co_argcount - len(func.__defaults__ or ())
    if 'method' in str(func.__class__): cnt -= 1
    return cnt


def get_func_id(func) -> T.FuncId:
    # related test: tests/duplicate_locals.py
    if config.duplicate_locals_scheme == 'exclusive':
        return str(id(func))
    else:
        # https://stackoverflow.com/a/46479810
        return func.__qualname__
