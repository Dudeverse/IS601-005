import numpy as np
import networkx as nx
from pulp import *

# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 1

def solve_vertex_cover_ip(G, vertex_costs):
    """Solves the vertex cover problem using an integer programming approach."""
    # Create a binary variable for each vertex indicating if it's in the vertex cover or not
    variables = LpVariable.dicts('x', G.nodes(), cat=LpBinary)
    # Create the optimization problem and the objective function
    prob = LpProblem("Vertex Cover", LpMinimize)
    prob += lpSum(variables[v] * vertex_costs[v] for v in G.nodes())
    # Add constraints to ensure that every edge is covered
    for u, v in G.edges():
        prob += variables[u] + variables[v] >= 1
    # Solve the problem
    prob.solve()
    # Extract the vertex cover from the solution
    vc = {v for v in G.nodes() if variables[v].value() == 1}
    return vc

for n in n_values:
    for q in q_values:
        for i in range(M):
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            
            # Solve the vertex cover problem using an integer programming approach
            vc = solve_vertex_cover_ip(G, vertex_costs)
            
            # Compute the total cost of the vertex cover and print it
            total_cost = sum(vertex_costs[v] for v in vc)
            print(f"Graph with n={n}, q={q},  with total cost {total_cost:.2f}")
