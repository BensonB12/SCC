# Kosaraju's Algorithm Implementation in Python

This project implements and tests Kosaraju's algorithm for finding strongly connected components in a directed graph. The graph is implemented as a class that supports various methods for graph manipulation and traversal, as well as producing the meta graph of strongly connected components.

## Graph Class

The `Graph` class supports the following functionality:

### Data Structures:
- **Node to Neighbors**: A dictionary mapping each node to its list of neighbors.
- **Edge to Weight**: A dictionary storing the weights of directed edges in the graph.

### Methods:

#### `add_node(node)`
- **Time Complexity**: `O(1)`
- Adds a node to the graph if it doesn't already exist.

#### `add_edge(node, neighbor, weight=1)`
- **Time Complexity**: `O(1)`
- Adds a directed edge from `node` to `neighbor` with the given weight (default is 1).
- If the edge already exists, its weight is updated.

#### `add_edges(edges)`
- **Time Complexity**: `O(E)` where E is the number of edges.
- Accepts a list of 2-tuples or 3-tuples, representing edges. Calls `add_edge()` for each edge.

#### `all_nodes()`
- **Time Complexity**: `O(V)` where V is the number of vertices.
- Returns a list of all nodes in the graph in the order they were added.

#### `all_edges()`
- **Time Complexity**: `O(E)`
- Returns a list of all directed edges in the graph in the order they were added.

#### `neighbors_of(node)`
- **Time Complexity**: `O(#neighbors)`
- Returns a list of the neighbors of the given node.

#### `edge_weight(node, neighbor)`
- **Time Complexity**: `O(1)`
- Returns the weight of the directed edge from `node` to `neighbor`. Returns `float('inf')` if there is no edge.

## Reversing the Graph

Write a function that:
- **Input**: An instance `G` of the `Graph` class.
- **Output**: An instance `G'` of the `Graph` class where all edges are reversed.
- **Time Complexity**: `O(V + E)`

## Meta Graph (Strongly Connected Components)

Write a function that:
- **Input**: An instance `G` of the `Graph` class.
- **Output**: An instance `G'` of the `Graph` class where each node in `G'` represents a strongly connected component (SCC) of `G`. Each node in `G'` should be a `frozenset` of nodes that are in the same SCC.
- **Time Complexity**: `O(V + E)`
- The nodes returned by `all_nodes()` should be a topological sort of `G'`.

## Kosaraju's Algorithm

Kosaraju's algorithm is implemented in two steps:
1. **First Pass (Reverse Graph and DFS)**: Perform a DFS on the reversed graph to determine the finishing times of nodes.
2. **Second Pass (Original Graph and DFS on Finish Times)**: Perform a DFS on the original graph in the order of decreasing finishing times to discover the strongly connected components.

## Testing with Pytest

To ensure the correctness of the implementation, `pytest` is used for testing the following cases:
- **Adding Nodes and Edges**: Ensure that nodes and edges are added correctly.
- **Reversing the Graph**: Ensure that the graph is correctly reversed.
- **Finding SCCs**: Ensure that the algorithm correctly finds all strongly connected components and constructs the meta graph.

### Running Tests

You can run the tests using `pytest` as follows:

```bash
pytest
