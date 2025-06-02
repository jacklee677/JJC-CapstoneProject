def load(path):
    vertexes = []
    edges = {}
    with open(path, 'r') as file:
        for line in file:
            province, problem, u, v, weight = line.strip().split(',')
            weight = float(weight)
            vertexes.append(u)
            vertexes.append(v)
            edges[(u, v)] = weight
            edges[(v, u)] = weight
    vertexes = sorted(list(set(vertexes)))
    minimum = min(edges.values())
    for u in vertexes:
        for v in vertexes:
            if (u, v) not in edges:
                if u == v:
                    edges[(u, v)] = 1.00
                else:
                    edges[(u, v)] = minimum
    return [[edges[(u, v)] for v in vertexes] for u in vertexes], vertexes


