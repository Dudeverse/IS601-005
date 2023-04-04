import numpy as np
import networkx as nx

# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 1

def greedy_vc(G):
    cover = set()
    total_cost = 0
    
    # Sort the vertices by their cost in decreasing order
    sorted_vertices = sorted(G.nodes.data('cost'), key=lambda x: x[1], reverse=True)
    
    for vertex, cost in sorted_vertices:
        # If the vertex is not covered by any previous vertex, add it to the cover
        if not any(vertex in cover for cover_vertex in cover):
            cover.add(vertex)
            total_cost += cost
    
    return cover, total_cost

def pricing_vc(G):
    cover = set()
    total_cost = 0
    
    # Compute the reduced cost of each vertex
    reduced_costs = {vertex: cost - sum(G.edges(vertex, data='cost', default=0).values()) for vertex, cost in G.nodes.data('cost')}
    
    while any(reduced_costs[vertex] < 0 for vertex in G.nodes):
        # Choose the vertex with the lowest reduced cost
        min_vertex = min(reduced_costs, key=reduced_costs.get)
        cover.add(min_vertex)
        total_cost += G.nodes[min_vertex]['cost']
        
        # Update the reduced cost of the neighboring vertices
        for neighbor in G.neighbors(min_vertex):
            reduced_costs[neighbor] -= G[min_vertex][neighbor]['cost']
    
    return cover, total_cost

for n in n_values:
    for q in q_values:
        for i in range(M):
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')
            
            # Compute the vertex cover and total cost using the greedy algorithm
            greedy_cover, greedy_cost = greedy_vc(G)
            
            # Compute the vertex cover and total cost using the pricing algorithm
            pricing_cover, pricing_cost = pricing_vc(G)
            
            # Print the graph with its vertex costs, and the vertex cover and total cost for both algorithms
            print(f"Graph with n={n}, q={q}, and vertex costs: {G.nodes.data('cost')}")
            print(f"Greedy vertex cover: {greedy_cover}, total cost: {greedy_cost}")
            print(f"Pricing vertex cover: {pricing_cover}, total cost: {pricing_cost}")
