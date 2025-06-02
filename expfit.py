import matplotlib.pyplot as plt
import math
import sympy

def fit(weights, infimum, flag = False):
    x = sorted([weight for weight in weights if weight > infimum])
    l, r = min(x), max(x)
    parameter = sympy.symbols('z')
    equation = sympy.Eq(sympy.exp(- parameter * l) / (sympy.exp(- parameter * l) - sympy.exp(- parameter * r)) * (r - l) - 1 / parameter, r - sum(x) / len(x))
    parameter = float(sympy.nsolve(equation, parameter, 1, tol = 1e-15))
    y = [1 - len(x) / len(weights) + len(x) / len(weights) * (math.exp(- parameter * l) - math.exp(- parameter * t)) / (math.exp(- parameter * l) - math.exp(- parameter * r)) for t in x]
    error = sum([(y[i] - (len(weights) - len(x) + i) / len(weights)) ** 2 for i in range(len(x))]) / len(x)
    if flag:
        plt.plot(weights, [i / len(weights) for i in range(len(weights))])
        plt.plot(x, y, color = 'red')
        plt.show()
    return parameter, error

def bestfit(weights, flag = False, sim = 0.90, eps = 0.03):
    weights = sorted(weights)
    n = int(math.sqrt(len(weights)))
    x = [sim * i / math.sqrt(n) for i in range(int(math.sqrt(n)))]
    w = [fit(weights, t) for t in x]
    y = [t[0] for t in w]
    z = [t[-1] for t in w]
    i = z.index(min(z, key = lambda t: abs(z[-1] + (z[0] - z[-1]) * eps - t)))
    if flag:
        plt.plot(x, z)
        plt.scatter(x[i], z[i])
        plt.show()
    infimum, parameter, error = x[i], y[i], z[i]
    return parameter, infimum