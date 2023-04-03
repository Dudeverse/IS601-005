import numpy as np
import networkx as nx

# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 1

def pricing_vc(G):
    # Initialize the vertex cover to an empty set
    cover = set()
    
    # Create a dictionary of vertices with their costs as values
    costs = dict(G.nodes.data('cost'))
    
    # Calculate the degree of each vertex
    degrees = dict(G.degree())
    
    # Create a set of uncovered vertices
    uncovered = set(G.nodes())
    
    # Create a dictionary of prices for vertices and edges
    prices = {v: 0 for v in uncovered}
    for u, v in G.edges():
        prices[(u, v)] = 0.5 * (costs[u] + costs[v])
    
    # Repeat until all vertices are covered
    while len(uncovered) > 0:
        # Solve the minimum cost perfect matching problem on the subgraph induced by the uncovered vertices
        subgraph = G.subgraph(uncovered)
        match = nx.algorithms.bipartite.matching.minimum_cost_matching(subgraph, weight=prices)
        
        # Find the set of vertices that are not covered by the matching
        non_matching_vertices = uncovered - set(match.keys()) - set(match.values())
        
        # Update the vertex cover and the set of uncovered vertices
        cover.update(set(match.keys()))
        cover.update(non_matching_vertices)
        uncovered.difference_update(cover)
        
        # Update the prices of vertices and edges
        for v in non_matching_vertices:
            prices[v] += min([prices[(u, v)] for u in set(G.neighbors(v)) & uncovered])
        for u, v in match.items():
            prices[(u, v)] -= prices[v]
            prices[(v, u)] -= prices[u]
    
    return cover

for n in n_values:
    for q in q_values:
        for i in range(M):
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')
            
            # Solve the vertex cover problem using pricing algorithm approach
            cover = pricing_vc(G)
            
            # Do whatever you want with the generated graph G and its vertex cover
            # For example, you can compute the size of the vertex cover and print it
            print(f"Graph with n={n}, q={q}, and vertex costs: {G.nodes.data('cost')} has a vertex cover of size {len(cover)}")
