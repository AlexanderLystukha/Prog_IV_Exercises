from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Node:

    def __init__(self, value: Any, left: Optional[Node], right: Optional[Node]):
        self.value: Any = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

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
