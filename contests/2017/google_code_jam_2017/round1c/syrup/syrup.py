#!/Users/slava/work/codejam2017/env/pypy3/bin/python

import math


def F(n, k, t, pancakes):
    #print(n, k, r, pancakes)
    ht, rt = pancakes[t]
    res = [(ht, rt)]

    for i in range(n-1, -1, -1):
        if len(res) == k:
            break

        if t != i:
            hi, ri = pancakes[i]
            if ri <= rt:
                res.append((hi, ri))

    surf = sum([2*p[0] * p[1] for p in res]) + res[0][1]**2
    #print(n, k, r, surf, res)
    return surf


def solve(n, k, pancakes):
    pancakes.sort()
    res = 0
    for t in range(n):
        res0 = F(n, k, t, pancakes)
        res = max(res, res0)

    return res * math.pi


for test in range(int(input())):
    n, k = [int(w) for w in input().split()]
    pancakes = [None]*n
    for i in range(n):
        r, h = [int(w) for w in input().split()]
        pancakes[i] = (h, r)

    res = solve(n, k, pancakes)

    print("Case #{}: {}".format(test+1, res))

