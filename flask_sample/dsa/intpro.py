import numpy as np
import networkx as nx
import pulp

def vertex_cover_ip(G):
    # Set up the integer programming problem
    lp = pulp.LpProblem("Vertex Cover", pulp.LpMinimize)
    x = {i: pulp.LpVariable(f"x{i}", cat="Binary") for i in G.nodes}
    lp += pulp.lpSum(G.nodes[v]['cost']*x[v] for v in G.nodes)
    for (i, j) in G.edges:
        lp += x[i] + x[j] >= 1

    # Solve the integer programming problem
    lp.solve()

    # Get the optimal vertex cover and its cost
    vertex_cover = [i for i in range(len(x)) if x[i].value() > 0.5]
    cost = pulp.value(lp.objective)

    return vertex_cover, cost

# Set the number of vertices and edge probability
n_vals = [160]
p_vals = [0.1 ,0.2, 0.3,0.4,0.5]
M = 1

# Generate M random graphs for each (n, p) combination
Count = 0
All_total_costs = []
n_list = []
p_list = []
for n in n_vals:
    for p in p_vals:
        for m in range(M):
            # Generate the graph
            Count = Count + 1
            G = nx.erdos_renyi_graph(n, p)

            # Assign a uniformly random cost between 0 and 1 to each vertex in the graph
            for v in G.nodes:
                G.nodes[v]['cost'] = np.random.uniform(0, 1)

            # Solve the vertex cover problem for the graph using integer programming
            vertex_cover, cost = vertex_cover_ip(G)
            total_cost = sum([G.nodes[v]['cost'] for v in vertex_cover])
            All_total_costs.append(total_cost)
            n_list.append(n)
            p_list.append(p)

            # Print the results
            print(f"Graph with {n} vertices and edge probability {p}:")
            print(f"Optimal vertex cover: {vertex_cover}")
            print(f"Cost of optimal vertex cover: {cost}\n")

print("****LP-ROUNDING results*****")
zipped = zip(n_list,p_list ,All_total_costs)


print(*zipped, sep ='\n')
print("****LP-ROUNDINGresults*****")