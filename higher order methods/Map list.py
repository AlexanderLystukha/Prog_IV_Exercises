import re
from typing import TypeVar, Callable
from typing import Callable

T = TypeVar("T")
B = TypeVar("B")
A = TypeVar("A")


def map_list(predicate: Callable[[T], int], my_list: list[T]) -> list[T]:
    return [item for item in my_list if predicate(item)]


# def predicate(d: str) -> int:
#     return int(d)

f = lambda x: x * 7

l = [3, 5, 7, 1, 2, 3, 7]
d: dict = {"hi": 3, "brandon": 3, "alec": 9999}

print(f'List: {list(map_list(f, l))}')


######################################

def map_dict(predicate: Callable[[T], int], dicto: dict) -> dict:
    for key, value in dicto.items():
        dicto[key] = predicate(value)
    return dicto


print(f'Dict: {map_dict(f, d)}')

#######################################

f = lambda x, y: x + y

def data_from_list_with(f: Callable[[B, B], B], kvs:list[tuple[A, B]]) -> dict[A, B]:

    newDicto: dict = {}
    for key, value in kvs:
        if newDicto[key] is not None:
            newDicto[key] = f(newDicto[key], value)
        else:
            newDicto[key] = value

    return newDicto

