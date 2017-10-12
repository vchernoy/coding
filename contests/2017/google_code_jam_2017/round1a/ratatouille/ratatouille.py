#!/Users/slava/work/codejam2017/env/py3/bin/python

import math


def func(graph, p, tab):
    best_res = 0
    l = tuple(graph)
    if l in tab:
        return tab[l]

    for e in l:
        j0, j1 = e
        removed = set()
        removed.add(e)
        for ex in l:
            if ex[0] == j0 or ex[1] == j1:
                removed.add(ex)
                graph.remove(ex)

        res = func(graph, p, tab) + 1
        best_res = max(best_res, res)

        graph.update(removed)

    tab[l] = best_res
    return best_res


def solve2(n, p, r, q):
    assert n == 2

    graph = set()

    for j0 in range(p):
        m0 = (q[0][j0] / (1.1 * r[0]), q[0][j0] / (0.9 * r[0]))
        for j1 in range(p):
            m1 = (q[1][j1] / (1.1 * r[1]), q[1][j1] / (0.9 * r[1]))

            m = (max(m0[0], m1[0]), min(m0[1], m1[1]))

            m = (math.ceil(m[0]), math.floor(m[1]))
            if m[0] <= m[1]:
                graph.add((j0,j1))

    return func(graph, p, {})


def solve1(n, p, r, q):
    assert n == 1

    graph = set()

    for j0 in range(p):
        m = (q[0][j0] / (1.1 * r[0]), q[0][j0] / (0.9 * r[0]))
        m = (math.ceil(m[0]), math.floor(m[1]))
        if m[0] <= m[1]:
            graph.add(j0)

    return len(graph)


def solve(n, p, r, q):
    if n == 1:
        return solve1(n, p, r, q)

    return solve2(n, p, r, q)

for test in range(int(input())):
    n, p = [int(w) for w in input().split()]
    r = [int(w) for w in input().split()]
    assert len(r) == n

    q = []
    for i in range(n):
        qi = [int(w) for w in input().split()]
        assert len(qi) == p
        q.append(qi)

    assert len(q) == n

    res = solve(n, p, r, q)

    print("Case #{}: {}".format(test+1, res))

