# a2_q3

from a2_q1 import *
import time

counter = 0
counter2 = 0

def gen_rand_graph(p):
	global counter
	global counter2

	for i in range(0,6):
		g = rand_graph(p, 31)
		print("  ")
		opt_bt = bt(g)
		print_q3(opt_bt)
		print("average number of neighbors : ", neighbors(g))
		print("  ")
		counter = 0
		counter2 = 0

def print_q3(opt_bt):
	result = opt_bt[0]
	c = opt_bt[2]
	num_teams = teams(result)
	running_time = opt_bt[1]
	assigned_count2 = counter2
	unassigned_count = counter
	print("number of teams :\t",num_teams)
	print("running time :\t",running_time)
	print("number of assigned :\t", counter2)
	print("number of unassigned :\t", unassigned_count)

def create_CSP(graph, m):
	teams = []
	for i in range(0,m+1):
		teams.append(i)
	csp = MapColoringCSP(teams, graph)
	return csp

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):

    def backtrack(assignment):
        global counter
        global counter2
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                counter2 += 1
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result != None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        counter += 1
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result


def bt(g):
	time_taken = []
	for i in range(0,len(g)):
		next_c = create_CSP(g , i)

		start_time = time.time()
		opt_bt = backtracking_search(next_c, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
		elapsed_time = time.time() - start_time

		time_taken.append(elapsed_time)
		if (opt_bt != None):
			running_time = 0
			for i in range(0,len(time_taken)):
				running_time += time_taken[i]
			return opt_bt, running_time, next_c
		else:
			continue

def neighbors(g):
	total_neighbors = 0
	for i in range(0,len(g)):
		total_neighbors += len(g[i])
	average_neighbors = total_neighbors/len(g)
	return average_neighbors

def teams(bt):
	team_set = set()
	for i in range(0,len(bt)):
		team_set.add(bt[i])
	num_teams = len(team_set)
	return num_teams

def run_q3():
	for i in range(0,6):
		print("*********************************************************")
		p = (i+1)/10
		print("When p =",p)
		print("*********************************************************")
		gen_rand_graph(p)


run_q3()

