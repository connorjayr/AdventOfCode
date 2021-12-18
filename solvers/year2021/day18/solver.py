from dataclasses import dataclass
from typing import Iterator, Optional
from util import *


@dataclass
class Node:
    value: Optional[int] = None
    parent: "Optional[Node]" = None
    left: "Optional[Node]" = None
    right: "Optional[Node]" = None

    def __str__(self) -> str:
        if self.value is not None:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"

    def find_left_sibling(self) -> "Optional[Node]":
        sibling = self

        while sibling.parent is not None and sibling.parent.left is sibling:
            sibling = sibling.parent
        if sibling.parent is None:
            return None

        sibling = sibling.parent.left
        while sibling.right is not None:
            sibling = sibling.right
        return sibling

    def find_right_sibling(self) -> "Optional[Node]":
        sibling = self

        while sibling.parent is not None and sibling.parent.right is sibling:
            sibling = sibling.parent
        if sibling.parent is None:
            return None

        sibling = sibling.parent.right
        while sibling.left is not None:
            sibling = sibling.left
        return sibling


def parse_num(num: str) -> Node:
    try:
        return Node(int(num))
    except ValueError:
        pass

    level = 0
    idx = 0
    while idx < len(num):
        c = num[idx]
        if c == "[":
            level += 1
        elif c == "]":
            level -= 1
        elif c == "," and level == 1:
            left = parse_num(num[1:idx])
            right = parse_num(num[idx + 1 : -1])
            node = Node(left=left, right=right)
            left.parent = node
            right.parent = node
            return node
        idx += 1


def explode(node: Node, depth: int = 0) -> bool:
    if node is None:
        return False

    if node.value is None and depth >= 4:
        left_sibling = node.find_left_sibling()
        if left_sibling is not None:
            left_sibling.value += node.left.value

        right_sibling = node.find_right_sibling()
        if right_sibling is not None:
            right_sibling.value += node.right.value

        node.value = 0
        node.left = None
        node.right = None
        return True

    return explode(node.left, depth + 1) or explode(node.right, depth + 1)


def split(node: Node) -> bool:
    if node is None:
        return False

    if node.value is not None and node.value >= 10:
        node.left = Node(node.value // 2, node)
        node.right = Node((node.value + 1) // 2, node)
        node.value = None
        return True

    return split(node.left) or split(node.right)


def reduce(root: Node):
    while True:
        if explode(root):
            continue
        if split(root):
            continue
        break


def magnitude(node: Node) -> int:
    if node.value is not None:
        return node.value
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def solve(input: Optional[str]) -> Iterator[any]:
    nums = input.split("\n")

    total = parse_num(nums[0])
    for num in nums[1:]:
        total = Node(left=total, right=parse_num(num))
        total.left.parent = total
        total.right.parent = total
        reduce(total)
    yield magnitude(total)

    max_magnitude = -math.inf
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            sum = Node(left=parse_num(nums[i]), right=parse_num(nums[j]))
            sum.left.parent = sum
            sum.right.parent = sum
            reduce(sum)

            max_magnitude = max(max_magnitude, magnitude(sum))
    yield max_magnitude
