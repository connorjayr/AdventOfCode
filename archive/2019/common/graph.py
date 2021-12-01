class Graph:
  def __init__(self):
    self.adj_list = {}

  def add_node(self, node):
    self.adj_list.setdefault(node, [])

  def add_edge(self, parent, child):
    self.add_node(parent)
    self.add_node(child)
    self.adj_list[parent].append(child)

  def get_nodes(self) -> list:
    return list(self.adj_list.keys())
  
  def get_children(self, parent):
    return self.adj_list[parent]