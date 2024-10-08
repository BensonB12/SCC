from typing import List
from graph import Graph

def whatever_first_search(graph: Graph, starting_node: int, ending_node: int, things_to_search: List):
  visited = set()
  search_edges = []
  things_to_search.append((None, starting_node)) # when I push I add in the score (plus the weight of the edge)
  while things_to_search:
    came_from, next_to_search = things_to_search[len(things_to_search) - 1]
    search_edges.append((came_from, next_to_search)) # need to update
    if next_to_search == ending_node:
      return search_edges
    visited.add(next_to_search)
    for neighbor in graph.neighbors_of(next_to_search):
      if neighbor not in visited:
        things_to_search.append((next_to_search, neighbor))
  return search_edges


def topological_sort_of_dag(graph: Graph, visit_order: List[int], flatten=True):
  graph = reverse_graph(graph)
  visited = set()
  post_order = []
  components = []

  def explore(node):
    visited.add(node)
    if graph.neighbors_of(node) is None: 
      return
    for neighbor in graph.neighbors_of(node):
      if neighbor not in visited:
        explore(neighbor)
    post_order.append(node)

  for node in visit_order:
    if node not in visited:
      explore(node)
      components.append(post_order)
      post_order = []

  if flatten:
    return [node for component in components for node in component]
  else:
    return components


# whatever_first_search(g, start, stack())
# whatever_first_search(g, start, queue())
# whatever_first_search(g, start, priority_queue())


def reverse_graph(graph: Graph):
  new_graph = Graph()
  for node in graph.all_nodes():
    new_graph.add_node(node)
    
  for edge in graph.all_edges():
    new_graph.add_edge(edge[1], edge[0])

  return new_graph


