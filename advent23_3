import sys
from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt


sys.setrecursionlimit(10000)
G = nx.Graph()
links = set()
adj = defaultdict(set)
with open("input/advent23.txt", "r") as file:
    for line in file:
        n1, n2 = line.strip().split("-")
        links.add((n1, n2))
        adj[n1].add(n2)
        adj[n2].add(n1)

G.add_edges_from(links)
cliques = list(nx.find_cliques(G))
print(cliques)

largest_clique = max(cliques, key=len)

pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_nodes(G, pos, alpha=0.5)

# Highlight the nodes in the largest clique
nx.draw_networkx_nodes(G, pos, nodelist=largest_clique, node_color='orange')

nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()

print("All cliques:", cliques)
print("Largest clique:", largest_clique)
print(",".join(sorted(largest_clique)))
