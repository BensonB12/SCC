from typing import Dict, List, Tuple

from edge import Edge


class Graph():
  # Nodes are represented by integers
  def __init__(self):
    self.node_to_neighbors: Dict[int, List[int]] = {}
    self.edge_to_wight: Dict[Tuple[int, int], int] = {}

  def add_node(self, node: int):
    if self.node_to_neighbors.get(node) is None:
      self.node_to_neighbors[node] = []

  def add_edge(self, node: int, neighbor: int, weight=1):
    if self.node_to_neighbors.get(node) is None or self.node_to_neighbors.get(neighbor) is None:
      return
    self.node_to_neighbors[node].append(neighbor)
    self.edge_to_wight[(node, neighbor)] = weight

  def add_edges(self, edges: List[Edge]):
    for edge in edges:
      self.add_edge(edge.node, edge.neighbor, edge.weight)

  def all_nodes(self):
    return self.node_to_neighbors.keys
  
  def all_edges(self):
    return self.edge_to_wight.keys
  
  def neighbors_of(self, node: int):
    return self.node_to_neighbors.get(node)
  
  def edge_weight(self, node: int, neighbor: int):
    return self.edge_to_wight.get((node, neighbor))
  