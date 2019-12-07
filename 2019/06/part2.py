import sys

class Graph:
  def __init__(self):
    self.adj_list = {}

  def add_node(self, node: str):
    self.adj_list.setdefault(node, [])

  def get_nodes(self):
    return self.adj_list.keys()
  
  def add_edge(self, parent: str, child: str):
    self.add_node(parent)
    self.add_node(child)
    self.adj_list[parent].append(child)
    self.adj_list[child].append(parent)

  def get_path_length(self, begin: str, end: str) -> int:
    length = 0
    visited = set(begin)
    queue = [begin]
    while end not in queue:
      level_length = len(queue)
      for _ in range(level_length):
        node = queue.pop(0)
        for child in self.adj_list[node]:
          if child not in visited:
            visited.add(child)
            queue.append(child)
      length += 1
    return length

graph = Graph()
with open(sys.argv[1], "r") as input_file:
  for edge in input_file.readlines():
    edge = edge.strip().split(")")
    graph.add_edge(edge[0], edge[1])

print(graph.get_path_length("YOU", "SAN") - 2)