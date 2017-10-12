#!/Users/slava/work/codejam2017/env/py3/bin/python


def solve0(n, e, s, dist, he, hs, src, tab):
    if src == n-1:
        return 0

    key = (he, hs, src)
    if key in tab:
        return tab[key]

    res = None
    for h1e, h1s in [(he, hs), (e[src], s[src])]:
        if h1e >= dist[src]:
            res1 = dist[src] / h1s + solve(n, e, s, dist, h1e - dist[src], h1s, src+1, tab)
            res = res1 if res is None else min(res, res1)

    tab[key] = res
    return res


def solve(n, e, s, d, he, hs, src, dst, tab):
    if src == n-1:
        return 0

    key = (he, hs, src, dst)
    if key in tab:
        return tab[key]

    res = None
    for h1e, h1s in [(he, hs), (e[src], s[src])]:
        if h1e >= d[src][v]:
            res1 = d[src][v] / h1s + solve(n, e, s, d, h1e - d[src][v], h1s, src+1, dst, tab)
            res = res1 if res is None else min(res, res1)

    tab[key] = res
    return res


for test in range(int(input())):
    n, q = [int(w) for w in input().split()]
    e = [0] * n
    s = [0] * n
    for i in range(n):
        ei, si = [int(w) for w in input().split()]
        e[i] = ei
        s[i] = si

    d = [None] * n
    for i in range(n):
        di = [int(w) for w in input().split()]
        #di = [x-1 if x > 0 else -1 for x in di]
        d[i] = di

    u = [0] * q
    v = [0] * q
    for i in range(q):
        ui, vi = [int(w)-1 for w in input().split()]
        u[i] = ui
        v[i] = vi

    if q == 1 and u[0] == 0 and v[0] == n-1:
        dist = [d[i][i+1] for i in range(n-1)]
        #print(d)
        #print(dist)
        res = solve(n, e, s, dist, 0, 0, 0, {})

    print("Case #{}: {}".format(test+1, res))
