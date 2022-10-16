import math
import random
import numpy as np

SEED_CONST = 42
N_CONST = 10
best_weight = math.inf
best_sol = []
nodes_visited = 1


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


def covers(p: list, sol, N):
    if not sol:
        return False
    sol_coverage = [False for i in range(N)]
    for i in sol:
        for j in p[i]:
            sol_coverage[j] = True
    return all(sol_coverage)


def solution(p: list, N):
    len_arr = [len(x) for x in p]
    act_sol = [0]
    act_weight = len(p[0])
    mark = [False for x in p]
    mark[0] = True
    solution_rec(p, N, len_arr, act_sol, act_weight, mark, 0, False)
    for i in range(len(p)):
        print(str(i) + ": " + str(p[i]))
    print(len_arr)
    print("Solution: " + str(best_sol))
    print("Weigth: " + str(best_weight))
    print("N. nodes " + str(nodes_visited))


def solution_rec(p: list, N, len_arr, act_sol, act_weight, mark, lvl, opt):
    global best_weight, nodes_visited, best_sol

    print("trying " + str(act_sol) + "; bw: " + str(best_weight) + "; aw: " + str(act_weight))
    nodes_visited += 1
    if covers(p, act_sol, N):
        if act_weight < best_weight:
            best_weight = act_weight
            best_sol = np.copy(act_sol)
            if act_weight == N:
                opt = True
            return

    if lvl > N: return

    for i in range(act_sol[-1] + 1, len(p)):
        if mark[i] or act_weight + len_arr[i] > best_weight:
            continue
        act_sol.append(i)
        mark[i] = True
        act_weight = act_weight + len_arr[i]
        solution_rec(p, N, len_arr, act_sol, act_weight, mark, lvl + 1, opt)
        if opt: return
        act_sol.pop()
        mark[i] = False
        act_weight = act_weight - len_arr[i]


solution(problem(N_CONST, SEED_CONST), N_CONST)
