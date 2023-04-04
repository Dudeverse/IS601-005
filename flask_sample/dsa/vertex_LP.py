import numpy as np
import networkx as nx
from pulp import *
from collections import defaultdict


# Define the possible values of n and q
n_values = [100, 120, 140, 160, 180, 200]
q_values = [0.5] #0.1 ,0.2, 0.3,0.4,0.5]

# Set the number of random graphs to generate
M = 1

def lp_vc(G):
    print("I'm running with LP approach!")
    # Create a binary variable for each vertex indicating whether it's in the vertex cover
    x = LpVariable.dicts('x', G.nodes(), lowBound=0, upBound=1, cat='Binary')
    
    # Create the LP problem and objective function
    prob = LpProblem('Vertex Cover LP', LpMinimize)
    prob += lpSum([G.nodes[v]['cost'] * x[v] for v in G.nodes()])
    
    # Add a constraint for each edge in the graph
    for (u, v) in G.edges():
        prob += x[u] + x[v] >= 1
    
    # Solve the LP problem
    prob.solve()
    
    # Check if the LP problem is infeasible
    if prob.status != LpStatusOptimal:
        raise ValueError('LP problem is infeasible')
    
    # Create a set of vertices in the vertex cover
    cover = set(v for v in G.nodes() if x[v].value() == 1)
    
    return cover


Count = 0
All_total_costs = []
n_list = []
q_list = []
for n in n_values:
    for q in q_values:
        for i in range(M):
            Count = Count + 1
            # Create a random graph with n nodes and edge probability q
            G = nx.erdos_renyi_graph(n, q)
            
            # Assign a random cost to each vertex, uniformly sampled from [0, 1]
            vertex_costs = np.random.uniform(size=n)
            nx.set_node_attributes(G, values=dict(zip(range(n), vertex_costs)), name='cost')


            print("LP ALGO RESULTS")

            # Solve the vertex cover problem using LP-based Rounding approach
            cover = lp_vc(G)
            
            # Calculate the total cost of the vertex cover
            total_cost = sum([G.nodes[v]['cost'] for v in cover])
            All_total_costs.append(total_cost)
            n_list.append(n)
            q_list.append(q)

            # Do whatever you want with the generated graph G and its vertex cover
            # For example, you can compute
            print(f"Graph with n={n}, q={q} and total cost {total_cost:.2f}")



zipped = zip(n_list,q_list ,All_total_costs)


print(*zipped, sep ='\n')