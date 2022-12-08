from functools import wraps
from time import perf_counter
from typing import Iterable
from sys import stdout


def timeit(func, file=stdout):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timeit(*args, **kwargs):
        print(f'run {func.__name__}({_unpack(args, kwargs)})', file=file)
        beg = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        print(f'got {res} in {end - beg:.10f} secs.\n', file=file)
        return res

    return wrapper_timeit


def _unpack(args: list, kwargs: dict) -> str:
    args = [f'{e!r}' for e in args]
    args.extend([f'{k}={v!r}' for k, v in kwargs.items()])
    return ', '.join(args)


def draw_memo(a: Iterable, b: Iterable, memo: list[list]):
    print('', *(f'{val:>3}' for val in b))
    for i, row in enumerate(memo):
        print(a[i], end='')
        print(*(f'{val:3}' for val in row))
