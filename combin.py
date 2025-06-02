from laod import load
import matplotlib.pyplot as plt
import torch
import random
import numpy as np
import bisect

weights, vertexes = load('SD_explore_ge_0.10.csv')

n = len(vertexes)

def f(i, j):
    t = 0
    for k in range(n):
        increasing = sorted(weights[k])
        l, r = weights[k][j], weights[k][i] + (weights[k][i] - weights[k][j])
        if l > r:
            l, r = r, l
        t += 1 - (bisect.bisect_right(increasing, r) - bisect.bisect_left(increasing, l)) / n
    return t / n

udex = []
for i in range(n):
    for j in range(n):
        if i != j and weights[i][j] > 0.75:
            udex.append(i)
            udex.append(j)
udex = list(set(udex))
print(len(udex))

t = []
for i in udex:
    for j in udex:
        if i != j:
            t.append([f(i, j), i, j])
    print(udex.index(i), '/', len(udex))
t = sorted(t)
t = t[ : : -1]
for z in t[ : 100]:
    print(z[0], vertexes[z[1]], vertexes[z[2]])

raise


values = [[[None for i in range(n)] for v in range(n)] for u in range(n)]
for i in range(n):
    increasing = sorted(weights[i])
    for u in range(n):
        for v in range(n):
            l, r = weights[i][v], weights[i][u] + (weights[i][u] - weights[i][v])
            if l > r:
                l, r = r, l
            values[u][v][i] = 1 - (bisect.bisect_right(increasing, r) - bisect.bisect_left(increasing, l)) / n
            print(values[u][v][i])
t = []
for u in range(n):
    for v in range(n):
        t.append([sum(values[u][v]) / n, (u, v)])
sorted(t)
for s in t[ : 30]:
    print((vertexes[s[-1][0]], vertexes[s[-1][1]]), s[0])