#!/usr/local/bin/pypy3

# !/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput, sys


def solve(n, m, k):
    res = []

    res.append(case1(n, m, k))
    res.append(case1(m, n, k))
    res.append(case2(n, m, k))
    res.append(case2(m, n, k))

    res = [r for r in res if r >= 0]

    return min(res) if len(res) > 0 else -1


def case1(n, m, k):
    if n < k+1:
        return -1

    if m < 2*k+3:
        return -1

    t = (n-1) // k

    return t+1


def case2(n, m, k):
    if n < 2*k+1:
        return -1

    if m < 2*k+3:
        return -1

    if k == 1:
        return 5

    return 4

def main():
    f = fileinput.input()

    for test in range(int(f.readline())):
        n, m, k = [int(w) for w in f.readline().split()]
        res = solve(n, m, k)
        print('Case #{}: {}'.format(test+1, res))


main()

