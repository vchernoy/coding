#!/bin/python3

import sys


def pr(a):
    for ax in a:
        print(ax)

def check(a, x1,y1,x2,y2):
    for x in range(x1, x2+1):
        if x > x1 and a[x][y1] < a[x-1][y2]:
            return False

        for y in range(y1+1, y2+1):
            if a[x][y] < a[x][y-1]:
                return False

    return True


def solve(a):
    n = len(a)
    m = len(a[0])

    lb = [[0] * m for _ in range(n)]
    for x in range(n):
        lb[x][0] = 0
        for y in range(1,m):
            if a[x][y] >= a[x][y-1]:
                lb[x][y] = lb[x][y-1]
            else:
                lb[x][y] = y

    pr(a)
    print()
    pr(lb)

    res = 0
    for x1 in range(n):
        for y1 in range(m):
            for y2 in range(y1,m):
                for x2 in range(x1,n):
                    valid = False
                    if lb[x2][y2] <= y1:
                        if x2 > x1:
                            if a[x2][y1] >= a[x2-1][y2]:
                                if x1 < x2 or y1 < y2:
                                    valid = True
                        else:
                            valid = True

                    if valid:
                        res += 1
                        print(x1,y1,x2,y2, check(a, x1,y1,x2,y2))
                    else:
                        break

    return res

if 0:
    n, m = 2, 2
    a = [[9,6],[7,6]]

    res = solve(a)
    print(res)

if 1:
    if __name__ == "__main__":
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        a = []
        for a_i in range(n):
            a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
            a.append(a_t)

        res = solve(a)
        print(res)
