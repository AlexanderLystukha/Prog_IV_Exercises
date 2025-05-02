import re
from typing import TypeVar, Callable

T = TypeVar("T")


def filter_list(predicate: Callable[[T], bool], my_list: list[T]) -> list[T]:
    return [item for item in my_list if predicate(item)]


def predicate(n) -> bool:
    return True if re.search(r"^\s*#", n) is None and re.search(r"^\s*$", n) is None else False


fh = open("hiii :3.txt")

lines = fh.readlines()

print(*list(filter_list(predicate, lines)))
