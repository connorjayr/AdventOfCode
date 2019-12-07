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

  def count_all_children(self, ancestor: str) -> int:
    queue = [ancestor]
    children = 0
    while len(queue) > 0:
      node = queue.pop(0)
      for child in self.adj_list[node]:
        queue.append(child)
        children += 1
    return children

graph = Graph()
with open(sys.argv[1], "r") as input_file:
  for edge in input_file.readlines():
    edge = edge.strip().split(")")
    graph.add_edge(edge[0], edge[1])

print(sum([graph.count_all_children(node) for node in graph.get_nodes()]))