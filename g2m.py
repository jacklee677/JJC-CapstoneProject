def gr2ma(path, threshold = 0):
    vertexes = []
    edges = {}
    ttt = []
    with open(path, 'r') as file:
        for line in file:
            province, problem, u, v, weight = line.strip().split(',')
            weight = float(weight)
            if weight >= threshold:
                ttt.append(u)
                ttt.append(v)
            vertexes.append(u)
            vertexes.append(v)
            edges[(u, v)] = weight
            edges[(v, u)] = weight
    vertexes = sorted(list(set(vertexes)))
    ttt = sorted(list(set(ttt)))
    for u in vertexes:
        for v in vertexes:
            if (u, v) not in edges:
                if u == v:
                    edges[(u, v)] = 1.00
                else:
                    edges[(u, v)] = 0.03
    return [[edges[(u, v)] for v in vertexes] for u in vertexes], [vertexes.index(t) for t in ttt]
