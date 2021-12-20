from collections import deque
from typing import Iterator, Optional
from util import *


def is_wall(pos: Vector[int], num: int) -> bool:
    num += pos[0] ** 2 + 3 * pos[0] + 2 * pos[0] * pos[1] + pos[1] + pos[1] ** 2
    return bin(num).count("1") % 2 == 1


def solve(input: Optional[str]) -> Iterator[any]:
    num = int(input)

    start = Vector[int](1, 1)
    end = Vector[int](31, 39)

    visited = set[Vector[int]]((start,))
    queue = deque[tuple[int, Vector[int]]](((0, start),))
    bbox = BoundingBox(Vector[int](0, 0), Vector[int](math.inf, math.inf))
    while len(queue) > 0:
        steps, pos = queue.popleft()
        if pos == end:
            yield steps
            break
        for neighbor in pos.neighbors(in_bbox=bbox):
            if is_wall(neighbor, num) or neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((steps + 1, neighbor))

    visited = set[Vector[int]]((start,))
    queue = deque[tuple[int, Vector[int]]](((0, start),))
    while len(queue) > 0:
        steps, pos = queue.popleft()
        if steps == 50:
            continue
        for neighbor in pos.neighbors(in_bbox=bbox):
            if is_wall(neighbor, num) or neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((steps + 1, neighbor))
    yield len(visited)
