import sympy
import matplotlib.pyplot as plt
import numpy as np
from expfit import bestfit

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
                    edges[(u, v)] = None
    return [[edges[(u, v)] for v in vertexes] for u in vertexes], vertexes

def evaluate(parameter, alpha, beta):
    if beta == None:
        beta = 0
    return (alpha - beta) * parameter

def solve(path):
    weights, vertexes = load(path)
    n = len(vertexes)
    items = sorted([[weights[i][j], (i, j)] for i in range(n) for j in range(n) if i != j and weights[i][j] != None])[ : : -1]
    components = [[i] for i in range(n)]
    alphas = [None for i in range(n)]
    betas = [None for i in range(n)]
    for [weight, (i, j)] in items:
        component = list(set(components[i] + components[j]))
        if len(component) == 2 and alphas[i] == None:
            alphas[i] = weight
        if len(component) == 2 and alphas[j] == None:
            alphas[j] = weight
        if len(component) > 2 and betas[i] == None:
            betas[i] = weight
        if len(component) > 2 and betas[j] == None:
            betas[j] = weight
        if len(component) > 2:
            component = component[ : 3]
        components[i] = component
        components[j] = component
    parameter, infimum = bestfit([item[0] for item in items])
    ts = sorted([[evaluate(parameter, alphas[i], betas[i]), i] for i in range(n) if alphas[i] != None])[ : : -1]
    plt.scatter([alphas[t[-1]] for t in ts], [t[0] for t in ts], color = 'black', zorder = 0)
    st = [t for t in ts if vertexes[t[-1]] in ['SD-J02249', 'SD-J02255']]
    plt.scatter([alphas[t[-1]] for t in st], [t[0] for t in st], color = 'red')
    
    def fun(gpt, color):
        st = [t for t in ts if gpt in vertexes[t[-1]] or '{}-{}'.format(vertexes[t[-1]], gpt) in vertexes]
        plt.scatter([alphas[t[-1]] for t in st], [t[0] for t in st], color = color)
        for t in st:
            print(path, '@', vertexes[t[-1]], '({:.3f},{:.3f})'.format(alphas[t[-1]], t[0]))
        return st
    st += fun('kimi', 'violet')
    st += fun('chatgpt', 'blue')

    digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    oo = [[vertexes[t[-1]], alphas[t[-1]], t[0]] for t in ts if t[0] > 4 and t not in st and vertexes[t[-1]][-1] in digs]
    oo = sorted(oo)
    for o in oo:
        print(path, '#', o[0], '({:.3f},{:.3f})'.format(o[1], o[2]))

solve('SD_chain.csv')
solve('SD_explore.csv')
solve('SD_poker.csv')
solve('SD_sticks.csv')
plt.show()