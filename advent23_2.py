from collections import defaultdict

adj = defaultdict(set)
with open("input/advent23.txt", "r") as file:
    for line in file:
        n1, n2 = line.strip().split("-")
        adj[n1].add(n2)
        adj[n2].add(n1)


def bk(current_clique, candidates, exclusion):
    if len(candidates) == 0 and len(exclusion) == 0:
        return [current_clique]

    cliques = []
    for v in candidates.copy():
        cliques.extend(bk(current_clique.union({v}), candidates.intersection(adj[v]), exclusion.intersection(adj[v])))
        candidates.remove(v)
        exclusion.update(v)

    return cliques


max_cliques = bk(set(), set(adj.keys()), set())
max_clique = max(max_cliques, key=len)
password = ",".join(sorted(list(max_clique)))
print(password)  # aq,cc,ea,gc,jo,od,pa,rg,rv,ub,ul,vr,yy
