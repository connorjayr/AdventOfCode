from collections import deque
from typing import Iterator, Optional
from util import *
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Optional[Node]"
    prev: "Optional[Node]"


def solve(input: Optional[str]) -> Iterator[any]:
    # nums = [(int(n) * 811589153, idx) for idx, n in enumerate(input.split("\n"))]
    nums = [Node(int(n) * 811589153, None, None) for n in input.split("\n")]
    order = [int(n) * 811589153 for n in input.split("\n")]
    print(order)
    nums_count = len(nums)
    print(nums_count)
    vals = {}
    for idx in range(len(nums) - 1):
        nums[idx].next = nums[idx + 1]
        nums[idx + 1].prev = nums[idx]
        vals[nums[idx].value] = nums[idx]
    vals[nums[len(nums) - 1].value] = nums[len(nums) - 1]
    nums[-1].next = nums[0]
    nums[0].prev = nums[-1]
    for itr in range(10):
        print(itr)
        for move in order:
            # print("moving", move)
            # head = vals[0]
            # for _ in range(nums_count):
            #     print(head.value, end=" ")

            #     head = head.next
            # print()
            idx = vals[move]
            ptr = idx
            if idx.value % (nums_count) == 0:
                continue
            for _ in range(abs(idx.value % (nums_count))):
                ptr = ptr.next if idx.value > 0 else ptr.prev
            # if idx.value < 0:
            #     ptr = ptr.prev
            idx.prev.next = idx.next
            idx.next.prev = idx.prev
            tmp = ptr.next
            ptr.next = idx
            idx.prev = ptr
            idx.next = tmp
            tmp.prev = idx

        # while idx < len(nums):
        #     # print(nums)
        #     # while idx < len(nums) and nums[idx][1]:
        #     #     idx += 1
        #     if idx == len(nums):
        #         break
        #     index = None
        #     for idx1 in range(len(nums)):
        #         if nums[idx1][1] == idx:
        #             index = idx1
        #     next = nums.pop(index)[0]
        #     new_idx = (index + next) % len(nums)
        #     nums = nums[:new_idx] + [(next, idx)] + nums[new_idx:]
    # zero_idx = None
    # for idx, node in enumerate(nums):
    #     if node.value == 0:
    #         zero_idx = idx
    sumz = 0
    zero = vals[0]
    for _ in range(3):
        for a in range(1000):
            zero = zero.next
        print(zero.value)
        sumz += zero.value
    yield sumz
    yield sumz
    # yield sum(nums[(zero_idx + idx) % len(nums)][0] for idx in (1000, 2000, 3000))
