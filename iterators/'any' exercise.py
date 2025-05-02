from typing import Callable, Iterable, TypeVar

A = TypeVar("A")


# def calculus_gulp(i: int) -> bool:
#     return i % 2 == 0


def any_with(f: Callable[[A], bool], i: Iterable[A]) -> bool:
    for num in i:
        if f(num):
            return True

    return False

list = [1, 2, 3, 4, 5, 6, 7]
print(any_with(lambda x: x % 2 == 0, list))
