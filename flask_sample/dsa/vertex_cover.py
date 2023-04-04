import numpy as np
import networkx as nx
from pulp import *
from collections import defaultdict


# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 2

def greedy_vc(G):
    print("I'm running!")
    """Solves the vertex cover problem using a greedy approach."""
    vc2 = set()  # start with an empty vertex cover
    # Sort the vertices by their degree in non-increasing order
    vertices = sorted(G.nodes(), key=lambda v: G.degree(v), reverse=True)
    for v in vertices:
        # If the current vertex is not covered, add it to the vertex cover and cover its neighbors
        if v not in vc2:
            vc2.add(v)
            vc2.update(G.neighbors(v))
    return vc2


def pricing_vc(G):
    print("I'm running too!")
    # Initialize the vertex cover to an empty set
    cover = set()
    
    # Create a dictionary of vertices with their costs as values
    costs = dict(G.nodes.data('cost'))
    
    # Create a list of edges with their costs as values
    edge_costs = [(u, v, costs[u] + costs[v]) for (u, v) in G.edges()]
    
    # Sort the list of edges in decreasing order of their costs
    edge_costs.sort(key=lambda x: x[2], reverse=True)
    
    # Create a set of uncovered vertices
    uncovered = set(G.nodes())
    
    # Repeat until all edges are covered
    while len(edge_costs) > 0:
        # Select the edge with the highest cost
        (u, v, _) = edge_costs[0]
        
        # Add the two endpoints of the edge to the cover
        cover.add(u)
        cover.add(v)
        
        # Remove the edge and its endpoints from the uncovered set
        edge_costs.pop(0)
        uncovered.discard(u)
        uncovered.discard(v)
        
        # Remove from the list of edges any edge that is incident on u or v
        edge_costs = [(a, b, c) for (a, b, c) in edge_costs if a != u and a != v and b != u and b != v]
    
    return cover





Count = 0
All_total_costs = []
for n in n_values:
    for q in q_values:
        for i in range(M):
            Count = Count + 1
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')
            


            print("GREEDY ALGO RESULTS")

            # Solve the vertex cover problem using the greedy approach and the Integer Programming approach
            vc_greedy = greedy_vc(G)
            
            # Compute the total cost of the vertex cover and print it
            total_cost_greedy = sum(vertex_costs[v] for v in vc_greedy)
            print(f"Graph with n={n}, q={q} total GREEDY COST {total_cost_greedy:.2f}")
            print()


            print("PRICING ALGO RESULTS")
            
            # Solve the vertex cover problem using pricing algorithm approach
            cover = pricing_vc(G)
            
            # Calculate the total cost of the vertex cover
            total_cost = sum([G.nodes[v]['cost'] for v in cover])
            
            # Do whatever you want with the generated graph G and its vertex cover
            # For example, you can compute the size and cost of the vertex cover and print them
            print(f"Graph with n={n}, q={q} and total cost {total_cost:.2f}")
            print("*************************************************************")


