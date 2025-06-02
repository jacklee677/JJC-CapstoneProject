import math

path = 'SD_explore_ge_0.10.csv'

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
vertexes = list(set(vertexes))
for u in vertexes:
    for v in vertexes:
        if (u, v) not in edges:
            if u == v:
                edges[(u, v)] = 1.0
            else:
                edges[(u, v)] = 1e-6

def kl(u, v):
    s = 0
    for t in vertexes:
        s += edges[(u, t)] * math.log(edges[(u, t)] / edges[(v, t)])
    return s / len(vertexes)

a = []
for u in vertexes:
    print('{:6.3f}%'.format(vertexes.index(u) / len(vertexes) * 100))
    for v in vertexes:
        if u != v:
            a.append([abs(kl(u, v)), (u, v)])
a = sorted(a)

with open('result{}.txt'.format(path), 'w') as file:
    for [s, (u, v)] in a:
        line = '{} {} {:.9f} : {:.9f}'.format(u, v, s, edges[(u, v)])
        print(line)
        file.write(line + '\n')