from ..common.graph import Graph
import sys

def count_all_children(graph: Graph, ancestor: str) -> int:
  queue = [ancestor]
  children = 0
  while len(queue) > 0:
    node = queue.pop(0)
    for child in graph.get_children(node):
      queue.append(child)
      children += 1
  return children

def get_path_length(graph: Graph, begin: str, end: str) -> int:
  length = 0
  visited = set(begin)
  queue = [begin]
  while end not in queue:
    level_length = len(queue)
    for _ in range(level_length):
      node = queue.pop(0)
      for child in graph.get_children(node):
        if child not in visited:
          visited.add(child)
          queue.append(child)
    length += 1
  return length

directed_graph = Graph()
undirected_graph = Graph()
with open(sys.argv[1], "r") as input_file:
  for edge in input_file:
    edge = edge.strip().split(")")
    
    directed_graph.add_edge(edge[0], edge[1])

    undirected_graph.add_edge(edge[0], edge[1])
    undirected_graph.add_edge(edge[1], edge[0])

# PART 1
print(sum([count_all_children(directed_graph, node) for node in directed_graph.get_nodes()]))
# PART 2
print(get_path_length(undirected_graph, "YOU", "SAN") - 2)