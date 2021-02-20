######################################################################
import functools


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

######################################################################

from typing import List

@debug
def how_many_different_numbers(s: List[int]) -> int:
    """ returns the number of unique elements in list s"""
    return len(set(s))

if __name__ == "__main__":
    # testing
    print(how_many_different_numbers([1, 2, 4, 1, 2, 4, 5]))
