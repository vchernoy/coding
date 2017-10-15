
def f(M, N):
    assert(M <= N)

    d = {}

    def f(m):
        assert(m >= 0)
        assert(m <= N)

        res = d.get(m, -1)
        if res == -1:
            if m == N:
                res = 0
            elif m == 0:
                res = 2**(N+1) - 2
            else:
                res = (f(m+1) + f(0)) / 2 + 1

            d[m] = res

        return res

    return f(M)


for t in xrange(int(raw_input())):
    N, M = [int(w) for w in raw_input().split()]
    print "%d.00" % f(M, N)

