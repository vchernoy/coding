
def F(m, n, x, up):
    global s, d, D, M

    assert(x >= 1)
    assert(x <= s)
    assert(n >= 1)

    k = (m, n, x, up)
    r = D.get(k, -1)
    if r == -1:
        r = 0
        if n == 1:
            r = 1 if m == 1 else 0

        elif n == 2:
            r = 0
            if up:
                for y in xrange(max(1, x-d), x):
                    r = (r + F(m, n-1, y, True)) % M

            else:
                for y in xrange(x+1, min(s, x+d)+1):
                    r = (r + F(m, n-1, y, False)) % M

        else:
            if up:
                for y in xrange(max(1, x-d), x):
                    r = (r + F(m, n-1, y, True)) % M
                    if n > 2:
                        r = (r + F(m-1, n-1, y, False)) % M

            else:
                for y in xrange(x+1, min(s, x+d)+1):
                    r = (r + F(m, n-1, y, False)) % M
                    if n > 2:
                        r = (r + F(m-1, n-1, y, True)) % M

        D[k] = r

    return r

def compute(m, n, s, d):
    global M

    r = 0
    if n == 1:
        for x in xrange(1, s+1):
            r = (r + F(m, n, x, False)) % M

    else:
        for x in xrange(1, s+1):
            r = (r + F(m, n, x, False)) % M
            r = (r + F(m, n, x, True)) % M

    return r

M = 1000000007

for t in xrange(int(raw_input())):
    n, m, s, d = [int(w) for w in raw_input().split()]
    D = {}
    print compute(m, n, s, d)

