import numpy as np
import networkx as nx
import pulp

# Set the number of vertices and edge probability
n = 120
p = 0.1

# Generate two random graphs with n vertices and edge probability p
G1 = nx.erdos_renyi_graph(n, p)
G2 = nx.erdos_renyi_graph(n, p)

# Assign a uniformly random cost between 0 and 1 to each vertex in the graphs
for v in G1.nodes:
    G1.nodes[v]['cost'] = np.random.uniform(0, 1)
for v in G2.nodes:
    G2.nodes[v]['cost'] = np.random.uniform(0, 1)

# Solve the vertex cover problem for each graph using linear programming
lp1 = pulp.LpProblem("Vertex Cover 1", pulp.LpMinimize)
x1 = {i: pulp.LpVariable(f"x{i}", cat="Binary") for i in range(n)}
lp1 += pulp.lpSum(G1.nodes[v]['cost']*x1[v] for v in G1.nodes)
for (i, j) in G1.edges:
    lp1 += x1[i] + x1[j] >= 1
lp1.solve()

lp2 = pulp.LpProblem("Vertex Cover 2", pulp.LpMinimize)
x2 = {i: pulp.LpVariable(f"x{i}", cat="Binary") for i in range(n)}
lp2 += pulp.lpSum(G2.nodes[v]['cost']*x2[v] for v in G2.nodes)
for (i, j) in G2.edges:
    lp2 += x2[i] + x2[j] >= 1
lp2.solve()

# Print the optimal vertex covers and their costs for each graph
print("Optimal Vertex Cover for Graph 1: ")
print([i for i in range(n) if x1[i].value() > 0.5])
print("Cost of the Optimal Vertex Cover for Graph 1: ")
print(pulp.value(lp1.objective))

print("Optimal Vertex Cover for Graph 2: ")
print([i for i in range(n) if x2[i].value() > 0.5])
print("Cost of the Optimal Vertex Cover for Graph 2: ")
print(pulp.value(lp2.objective))
