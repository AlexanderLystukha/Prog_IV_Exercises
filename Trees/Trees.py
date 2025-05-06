from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional



@dataclass
class Node:

    def __init__(self, value: Any, left: Optional[Node], right: Optional[Node]):
        self.value: Any = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
        self.head: Node = self

    def __len__(self):
        length = 1

        if self.left is not None:
            length += len(self.left)

        if self.right is not None:
            length += len(self.right)

        return length

    def __contains__(self, item):
        if item == self.value:
            return True
        else:
            if self.left is not None and item < self.value:
                if item in self.left:
                    return True

            if self.right is not None and item > self.value:
                if item in self.right:
                    return True

        return False

    def go_left_until_forced_to_go_right(self):
        print(self.value)
        if self.left is not None:
            self.left.go_left_until_forced_to_go_right()

        if self.right is not None:
            self.right.go_left_until_forced_to_go_right()

        else:
            return

    def sort_tree(self):

        if self.left is not None:
            self.left.sort_tree()

        print(self.value)

        if self.right is not None:
            self.right.sort_tree()

        else:
            return

    def add(self, item):
        if item == self.value:
            return
        else:
            if self.left is not None and item < self.value:
                if not self.left:
                    self.left = Node(item)
                else:
                    self.left.add(item)

            if self.right is not None and item > self.value:
                if not self.right:
                    self.right = Node(item)
                else:
                    self.right.add(item)

    def tree_height(self, value: Node):
        left: int = 0
        right: int = 0

        if self.left is not None:
            left = self.tree_height(self.left) + 1

        if self.right is not None:
            right = self.tree_height(self.right) + 1

        return max(left, right)

    def subset(self, low, high) -> list:
        acc = []
        self._subset(self.head, low, high, acc)
        return acc

    def _subset(self, current,low, high, acc: list):
        if current.left is not None and low < current.value:
            self._subset(current.left, low, high, acc)

        if low <= current.value <= high:
            acc.append(current.value)

        if current.right is not None and low < current.value:
            self._subset(current.right, low, high, acc)


brandontree: Node = Node(15,
                         Node(10,
                              Node(8,
                                   Node(3, None, None),
                                   Node(9, None, None)),
                              Node(12,
                                   Node(11, None, None),
                                   Node(14, None, None))),
                         Node(20,
                              Node(17,
                                   Node(16, None, None),
                                   Node(18, None, None)),
                              Node(25, None, None)))

# if 0 in brandontree:
#     print("woohoo")
# else:
#     print("wompwomp")

print(brandontree.subset(3, 10))
