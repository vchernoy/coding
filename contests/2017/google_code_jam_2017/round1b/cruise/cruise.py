#!/Users/slava/work/codejam2017/env/py3/bin/python

def solve(d, n, k, s):
    h = [(k[i], s[i]) for i in range(n)]
    h.sort()

    t = 0
    k_, s_ = h[-1]
    for i in range(n-2, -1, -1):
        ki, si = h[i]
        di = d-ki
        d_ = d-k_
        ti = di / si
        t_ = d_ / s_

        if ti >= t_:
            k_, s_ = ki, si
        else:
            k_, s_ = ki, di / t_

    k0 = 0
    d0 = d
    t0 = 0

    d_ = d-k_
    t_ = d_ / s_
    k_, s_ = k0, d0 / t_
    return s_

for test in range(int(input())):
    d, n = [int(w) for w in input().split()]
    k = [0]*n
    s = [0]*n
    for i in range(n):
        ki, si = [int(w) for w in input().split()]
        k[i] = ki
        s[i] = si

    res = solve(d, n, k, s)

    print("Case #{}: {}".format(test+1, res))
