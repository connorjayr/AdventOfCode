import heapq
import sys

class Graph:
  def __init__(self):
    self.adj_list = {}
    self.rev_list = {}

  def add_node(self, node):
    if node in self.adj_list: return
    self.adj_list[node] = []
    self.rev_list[node] = []

  def add_edge(self, parent, child):
    self.add_node(parent)
    self.add_node(child)

    self.adj_list[parent].append(child)
    self.rev_list[child].append(parent)

  def get_children(self, parent):
    return self.adj_list[parent]

  def get_parents(self, child):
    return self.rev_list[child]

  def get_sources(self):
    sources = []
    for node, parents in self.rev_list.items():
      if len(parents) == 0:
        sources.append(node)
    return sources

graph = Graph()

with open(sys.argv[1], "r") as input_file:
  for edge in input_file.readlines():
    edge = edge.split()
    graph.add_edge(edge[1], edge[7])

queue = graph.get_sources()
queue.sort()
visited = set(queue)
while len(queue) > 0:
  i = 0
  remove = False
  while not remove:
    remove = True
    for parent in graph.get_parents(queue[i]):
      if parent not in visited:
        remove = False
        break
    if not remove:
      i += 1

  node = queue.pop(i)
  print(node, end="")
  visited.add(node)
  for child in graph.get_children(node):
    if child in queue or child in visited: continue
    queue.append(child)
  queue.sort()
print()