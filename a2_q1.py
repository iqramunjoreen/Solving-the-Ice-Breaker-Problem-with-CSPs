# a2_q1.py

from csp import *

import time

def pick(p):
    weighted_random = ['no_pick'] * int(100 - p * 100) + ['pick'] * int(p * 100)
    result = random.choice(weighted_random)
    return result

def rand_graph(p, n):
    graph = {}
    for i in range(0, n):
        graph[i] = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if (pick(p) == 'pick'):
                graph[i].append(j)
                graph[j].append(i)
    return graph
    


