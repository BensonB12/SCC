from typing import Set, Dict, List, FrozenSet
from graph import Graph
from search import topological_sort_of_dag, reverse_graph

def find_strongly_connected_components(graph: Graph) -> List[FrozenSet[int]]:
    visited = set()
    post_order = []
    
    def dfs(node: int):
        visited.add(node)
        for neighbor in graph.neighbors_of(node) or []:
            if neighbor not in visited:
                dfs(neighbor)
        post_order.append(node)

    # Step 1: Perform DFS to compute post-order in the original graph
    for node in graph.all_nodes():
        if node not in visited:
            dfs(node)

    # Step 2: Reverse the graph
    reversed_graph = reverse_graph(graph)

    # Step 3: Perform DFS on the reversed graph in decreasing order of post-order
    visited.clear()
    sccs = []

    def explore_scc(node: int, scc: Set[int]):
        visited.add(node)
        scc.add(node)
        for neighbor in reversed_graph.neighbors_of(node) or []:
            if neighbor not in visited:
                explore_scc(neighbor, scc)

    while post_order:
        node = post_order.pop()
        if node not in visited:
            scc = set()
            explore_scc(node, scc)
            sccs.append(frozenset(scc))

    return sccs


def build_meta_graph(graph: Graph) -> Graph:
    sccs = find_strongly_connected_components(graph)
    
    # Create a mapping from nodes to their SCCs
    node_to_scc: Dict[int, FrozenSet[int]] = {}
    for scc in sccs:
        for node in scc:
            node_to_scc[node] = scc

    # Create the meta-graph G'
    meta_graph = Graph()
    
    # Add each SCC as a node in the meta-graph
    for scc in sccs:
        meta_graph.add_node(scc)

    # Add edges between SCCs based on the original graph's edges
    for node in graph.all_nodes():
        for neighbor in graph.neighbors_of(node) or []:
            node_scc = node_to_scc[node]
            neighbor_scc = node_to_scc[neighbor]
            if node_scc != neighbor_scc:
                meta_graph.add_edge(node_scc, neighbor_scc)

    # Return meta-graph (G')
    return meta_graph
