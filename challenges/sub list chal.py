from timeit import timeit
from typing import Callable, Optional, TypeVar

B = TypeVar("B")
A = TypeVar("A")


# @timeit
def foo(num_add, num_remove, s):
    s += num_add
    if num_remove is not None:
        s -= num_remove
    return s


# REMINDER: when writing the type hinting for callables, there are two parameters.
#
# ex: Callable[[x, y], z]
#
# the first argument of Callable is '[x, y]', which is the parameters that the callable (method) needs for
# functionality the second argument is 'z', which is the return value of the method

def get_sum(predicate: Callable[[A, Optional[A], B], B], stretch: int, s: B) -> list[B]:
    result: list[B] = []
    list_of_nums: list[int] = [1, 2, 7, 13, 20, 2, 8]
    for i in range(len(list_of_nums) - stretch + 1):
        if i < stretch:
            s = predicate(list_of_nums[i], None, s)
        else:
            result.append(s)
            s = predicate(list_of_nums[i], list_of_nums[i - stretch], s)

    result.append(s)
    return result
