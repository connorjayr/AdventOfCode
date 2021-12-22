import networkx as nx
from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    graph = nx.Graph()
    for line in input.split("\n"):
        source, dests = line.split(" <-> ")
        for dest in dests.split(", "):
            graph.add_edge(int(source), int(dest))

    yield len(nx.bfs_tree(graph, 0))
    yield nx.number_connected_components(graph)
