def stack():
  return []

def whatever_first_search(g, start, goal, things_to_search):
  visited = set()
  search_edges = []
  things_to_search.push((None, start)) # when I push I add in the score (plus the weight of the edge)
  while things_to_search:
    came_from, next_to_search = things_to_search.pop()
    search_edges.push((came_from, next_to_search)) # need to update
    if next_to_search == goal:
      return search_edges
    visited.add(next_to_search)
    for neighbor in g.get_neighbors(next_to_search):
      if neighbor not in visited:
        things_to_search.push((next_to_search, neighbor))
  return search_edges

# whatever_first_search(g, start, stack())
# whatever_first_search(g, start, queue())
# whatever_first_search(g, start, priority_queue())
