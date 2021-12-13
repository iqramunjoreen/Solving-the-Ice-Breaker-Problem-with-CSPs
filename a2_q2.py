# a2_q2.py

def check_teams(graph, csp_sol):
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if (csp_sol[i] == csp_sol[graph[i][j]]):
                return False
    return True
