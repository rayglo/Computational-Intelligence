import math
import random
import numpy as np

SEED_CONST = 42
N_CONST = 50
best_weight = math.inf
best_sol = []
nodes_visited = 0
opt = False


def h(node, prob, sol, N):
    "It calculates an heuristic based on how many elements of a node are not already in the solution"
    elements_sol = np.array([])
    for i in sol:
        elements_sol = np.append(elements_sol, prob[i])
    elements_sol = np.unique(elements_sol)
    len_sol = elements_sol.size
    elements_sol = np.unique(np.append(elements_sol, node))
    h_val = elements_sol.size - len_sol

    return h_val

def take_second(x):
    return x[1]


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


def covers(p: list, sol, N):
    """Just a check if a solution covers the set"""
    if not sol:
        return False
    sol_coverage = [False for i in range(N)]
    for i in sol:
        for j in p[i]:
            sol_coverage[j] = True
    return all(sol_coverage)


def solution(p: list, N):
    """Prepares the steps dor recursion"""
    len_arr = [len(x) for x in p]
    act_sol = []
    act_weight = 0
    mark = [False for x in p]
    solution_rec(p, N, len_arr, act_sol, act_weight, mark, 0)
    for i in range(len(p)):
        print(str(i) + ": " + str(p[i]))
    print(len_arr)
    print("Solution: " + str(best_sol))
    print("Weigth: " + str(best_weight))
    print("N. nodes " + str(nodes_visited))


def solution_rec(p: list, N, len_arr, act_sol, act_weight, mark, lvl):
    """It enumerates combinations of lists, trying to get the lists with more elements that misses from the actual solution
    And it stops after a certain depth. Lists are ranked based on an heuristic score, the lowest part of the scoreboard
    is excluded, and then the algorithm explores them in order. It is not 100% complete, but it works pretty well."""
    global best_weight, nodes_visited, best_sol, opt

    print("trying " + str(act_sol) + "; bw: " + str(best_weight) + "; aw: " + str(act_weight) + "; node=" + str(nodes_visited))
    if covers(p, act_sol, N):
        if act_weight < best_weight:
            best_weight = act_weight
            best_sol = np.copy(act_sol)
            if act_weight == N:
                opt = True
            return

    if lvl > N/2: return

    nodes_visited += 1

    h_vec = sorted([(i, h(p[i], p, act_sol, N)) for i in range(len(p))], key=take_second, reverse=True)

    #print(h_vec)

    for x in h_vec[:int(N/2)]:
        i = x[0]
        if mark[i] or act_weight + len_arr[i] > best_weight:
            continue
        act_sol.append(i)
        mark[i] = True
        act_weight = act_weight + len_arr[i]
        solution_rec(p, N, len_arr, act_sol, act_weight, mark, lvl + 1)
        if opt: return
        act_sol.pop()
        mark[i] = False
        act_weight = act_weight - len_arr[i]


solution(problem(N_CONST, SEED_CONST), N_CONST)
