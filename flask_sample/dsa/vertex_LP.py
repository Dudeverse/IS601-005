import numpy as np
import networkx as nx
from pulp import LpVariable, LpProblem, lpSum, GLPK, LpMinimize

# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Set the number of random graphs to generate
M = 100

def solve_vertex_cover_lp(G):
    # Initialize LP problem
    prob = LpProblem("Vertex Cover LP", LpMinimize)

    # Create a binary variable for each vertex
    vertex_vars = LpVariable.dicts("vertex", G.nodes(), lowBound=0, upBound=1, cat='Integer')

    # Define the objective function
    prob += lpSum(vertex_vars.values())

    # Add the constraint for each edge
    for u, v in G.edges():
        prob += vertex_vars[u] + vertex_vars[v] >= 1

    # Solve the LP problem
    prob.solve(GLPK(msg=0))

    # Extract the solution
    cover = [v for v in G.nodes() if vertex_vars[v].value() == 1]

    return cover

for n in n_values:
    for q in q_values:
        for i in range(M):
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)

            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')

            # Solve the vertex cover problem using LP-based Rounding
            cover = solve_vertex_cover_lp(G)

            # Print the results
            print(f"Graph with n={n}, q={q}, and vertex costs: {G.nodes.data('cost')} has VC of size {len(cover)}")
