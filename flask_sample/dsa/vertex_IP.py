import networkx as nx
import numpy as np
import random
# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 2


def pricing_vc(G):
    # Initialize a dictionary to keep track of nodes and their prices
    prices = {node: G.nodes[node]['cost'] for node in G.nodes()}
    
    # Initialize an empty set to hold the selected vertices
    selected = set()
    
    # Loop until all edges are covered
    while G.number_of_edges() > 0:
        # Choose a random uncovered edge
        edge_list = list(G.edges())
        random_edge = random.choice(edge_list)
        u, v = random_edge
        
        # Determine the lowest cost node between u and v
        if prices[u] < prices[v]:
            selected.add(u)
        else:
            selected.add(v)
        
        # Update the prices of the remaining nodes
        for node in G.nodes():
            if node not in selected:
                # Determine the minimum cost of edges adjacent to the node
                min_cost = np.inf
                for neighbor in G.neighbors(node):
                    if neighbor not in selected and prices[neighbor] < min_cost:
                        min_cost = prices[neighbor]
                
                # Set the price of the node to the minimum cost
                prices[node] = min_cost
    
        # Remove the edges covered by the selected vertices
        G.remove_edges_from(G.edges(selected))
    
    # Return the set of selected vertices
    return selected




for n in n_values:
    for q in q_values:
        for i in range(M):
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')
            
            # Solve the vertex cover problem using the pricing algorithm approach
            vc = pricing_vc(G)
            
            # Compute the total cost of the vertex cover and print it
            total_cost = sum(vertex_costs[v] for v in vc)
            print(f"Graph with n={n}, q={q}, with total cost {total_cost:.2f}")
