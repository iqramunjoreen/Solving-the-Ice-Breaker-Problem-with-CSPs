# a2_q4

from a2_q1 import *
import time

counter = 0

def gen_rand_graph(p):
	global counter
	global counter2
	for i in range(0,6):
		g = rand_graph(p, 150)
		print(" ")
		opt_bt = find_opt_bt(g)
		print_q4(opt_bt)
		print("average number neighbors :\t", neighbors(g))
		print(" ")
		counter = 0

def print_q4(opt_bt):
	result = opt_bt[0]
	c = opt_bt[2]
	num_teams = teams(result)
	running_time = opt_bt[1]
	assigned_count = counter
	
	print("number of teams :\t",num_teams)
	print(f'running time :\t{running_time}')
	print("number of assigned variables :\t", assigned_count)
	print("number of unassigned variables :\t", 0)

def min_conflicts(csp, max_steps=1000):
    """This function solves a CSP by schotastic hillclimbing on the number
    of conflicts"""
    global counter
    csp.current = current = {}
    for var in csp.variables:
        val = argmin_random_tie(csp.domains[var],
                key=lambda val: csp.nconflicts(var, val, current))
        csp.assign(var, val, current)
        counter += 1
    for i in range(max_steps):
        conflicted = csp.conflicted_vars(current)
        if not conflicted:
            return current
        var = random.choice(conflicted)
        val = min_conflicts_value(csp, var, current)
        csp.assign(var, val, current)
        counter += 1
    return None

def create_CSP(graph, m):
	teams = []
	for i in range(0,m+1):
		teams.append(i)
	csp = MapColoringCSP(teams, graph)
	return csp


def find_opt_bt(g):
	time_taken = []
	for i in range(0,len(g)):
		next_c = create_CSP(g , i)

		start_time = time.time()
		opt_bt = min_conflicts(next_c)
		elapsed_time = time.time() - start_time

		time_taken.append(elapsed_time)
		if (opt_bt != None):
			running_time = 0
			for i in range(0,len(time_taken)):
				running_time += time_taken[i]
			return opt_bt, running_time, next_c
		else:
			continue

def teams(bt):
	team_set = set()
	for i in range(0,len(bt)):
		team_set.add(bt[i])
	num_teams = len(team_set)
	return num_teams


def neighbors(g):
	total_neighbors = 0
	for i in range(0,len(g)):
		total_neighbors += len(g[i])
	average_neighbors = total_neighbors/len(g)
	return average_neighbors


def run_q4():
	for i in range(0,6):
		print("*********************************************************")
		p = (i+1)/10
		print("When p =",p)
		print("*********************************************************")
		gen_rand_graph(p)




run_q4()
