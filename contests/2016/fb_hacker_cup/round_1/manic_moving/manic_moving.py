#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput, sys


def add(x, y):
    if x is None or y is None:
        return None

    return x + y


def min_of(x, y):
    if x is None:
        return y

    if y is None:
        return x

    return min(x, y)


def compute(dist, s, d):
    k = len(s)
    tab_f = {}
    tab_g = {}

    def f(i):
        if i == k:
            return 0

        res = dist[s[i]][d[i]]
        if i == k - 1:
            return res

        if i in tab_f:
            return tab_f[i]

        res = add(res, dist[d[i]][s[i+1]])
        if res is not None:
            res = add(res, f(i+1))

        res2 = add(dist[s[i]][s[i+1]], dist[s[i+1]][d[i]])
        if res2 is not None:
            res2 = add(res2, g(d[i], d[i+1], i+2))

        res = min_of(res, res2)
        tab_f[i] = res

        return res

    def g(x, y, i):
        if i == k:
            return dist[x][y]

        key = (x, y, i)
        if key in tab_g:
            return tab_g[key]

        res = add(dist[x][y], dist[y][s[i]])
        if res is not None:
            res = add(res, f(i))

        res2 = add(dist[x][s[i]], dist[s[i]][y])
        if res2 is not None:
            res2 = add(res2, g(y, d[i], i+1))

        res = min_of(res, res2)
        tab_g[key] = res

        return res

    if dist[0][s[0]] is None:
        return None

    return add(f(0), dist[0][s[0]])


def find_min_dist(edges):
    n = len(edges)
    dist = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = edges[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

                dikj = add(dist[i][k], dist[k][j])
                dist[i][j] = min_of(dist[i][j], dikj)

    return dist


def main():
    f = fileinput.input()

    for test in range(int(f.readline())):
        n, m, k = [int(w) for w in f.readline().split()]
        edges = [[None] * n for _ in range(n)]
        for i in range(m):
            a, b, g = [int(w) for w in f.readline().split()]
            a -= 1
            b -= 1
            if edges[a][b] is not None:
                g = min(g, edges[a][b])

            edges[a][b] = edges[b][a] = g

        for i in range(n):
            edges[i][i] = 0

        s = [0] * k
        d = [0] * k
        for i in range(k):
            si, di = [int(w) for w in f.readline().split()]
            si -= 1
            di -= 1
            s[i] = si
            d[i] = di

        dist = find_min_dist(edges)

        res = compute(dist, s, d)
        if res is None:
            res = -1

        print('Case #{}: {}'.format(test+1, res))

print(sys.getrecursionlimit(), file=sys.stderr)
sys.setrecursionlimit(6000)

main()
