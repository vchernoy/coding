#!/Users/slava/work/codejam2017/env/py3/bin/python

import random


def extend(rect, a):
    r = len(a)
    c = len(a[0])

    ch, i0, j0, i1, j1 = rect

    ok = True
    while ok:
        ok = False
        if j0 >= 1:
            clean = True
            for i in range(i0, i1+1):
                if a[i][j0-1] != '?':
                    clean = False
                    break

            if clean:
                for i in range(i0, i1+1):
                    a[i][j0-1] = ch

                j0 -= 1
                ok = True

        if j1 < c - 1:
            clean = True
            for i in range(i0, i1+1):
                if a[i][j1+1] != '?':
                    clean = False
                    break

            if clean:
                for i in range(i0, i1+1):
                    a[i][j1+1] = ch

                j1 += 1
                ok = True

        if i0 >= 1:
            clean = True
            for j in range(j0, j1+1):
                if a[i0-1][j] != '?':
                    clean = False
                    break

            if clean:
                for j in range(j0, j1+1):
                    a[i0-1][j] = ch

                i0 -= 1
                ok = True

        if i1 < r - 1:
            clean = True
            for j in range(j0, j1+1):
                if a[i1+1][j] != '?':
                    clean = False
                    break

            if clean:
                for j in range(j0, j1+1):
                    a[i1+1][j] = ch

                i1 += 1
                ok = True

    return (ch, i0, j0, i1, j1)


def solve1(a):
    r = len(a)
    c = len(a[0])
    rects = []
    n_covered = 0
    for i in range(r):
        for j in range(c):
            if a[i][j] != '?':
                rect = (a[i][j], i, j, i, j)
                rects.append(rect)
                n_covered += 1

    random.shuffle(rects)

    while (n_covered < c*r) and rects:
        rect = rects.pop()
        rect1 = extend(rect, a)
        if rect != rect1:
            n_covered += sq(rect1) - sq(rect)

    return n_covered >= c*r


def solve(a):
    a0 = [row[:] for row in a]
    while not solve1(a):
        for i in range(r):
            for j in range(c):
                a[i][j] = a0[i][j]


def sq(rect):
    ch, i, j, i1, j1 = rect
    s = (i1 - i + 1) * (j1 - j + 1)
    assert s >= 1
    return s


random.seed()
for test in range(int(input())):
    r, c = [int(w) for w in input().split()]
    a = [None]*r
    for i in range(r):
        s = input().strip()
        a[i] = [ch for ch in s]
        # print(s)
        assert len(a[i]) == c

    solve(a)

    print("Case #{}:".format(test+1))
    for i in range(r):
        print(''.join(a[i]))





