from collections import defaultdict
from typing import Iterator, Optional
from util import *


def dfs(
    graph: dict[str, list[str]],
    cave: str,
    small_visited: defaultdict[str, int],
    visit_twice: bool,
):
    if cave == "end":
        return 1

    if cave.islower():
        if visit_twice:
            visits = small_visited.get(cave, 0)
            can_visit = visits == 0 or (
                visits == 1
                and cave != "start"
                and all(v < 2 for v in small_visited.values())
            )
        else:
            can_visit = small_visited.get(cave, 0) < 1
        if not can_visit:
            return 0

        small_visited[cave] += 1

    paths = 0
    for dest in graph[cave]:
        paths += dfs(graph, dest, small_visited, visit_twice)

    if cave.islower():
        small_visited[cave] -= 1

    return paths


def solve(input: Optional[str]) -> Iterator[any]:
    graph = defaultdict(list)
    for edge in input.split("\n"):
        a, b = edge.split("-")
        graph[a].append(b)
        graph[b].append(a)

    small_visited = defaultdict[str, int](int)
    yield dfs(graph, "start", small_visited, False)

    small_visited = defaultdict[str, int](int)
    yield dfs(graph, "start", small_visited, True)
