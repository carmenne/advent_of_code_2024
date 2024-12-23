from collections import defaultdict

adj = defaultdict(set)
with open("input/advent23.txt", "r") as file:
    for line in file:
        n1, n2  = line.strip().split("-")
        adj[n1].add(n2)
        adj[n2].add(n1)

print(adj)
links = set()
for k, v in adj.items():
    if k[0] == "t":
        for node1 in v:
            for node2 in adj[node1]:
                if k in adj[node2]:
                    links.add(tuple(sorted([k, node1, node2])))

print(len(links)) # 1064
