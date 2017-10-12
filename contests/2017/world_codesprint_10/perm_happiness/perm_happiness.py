# Enter your code here. Read input from STDIN. Print output to STDOUTimport sys
import itertools
import sys

sys.setrecursionlimit(10000)

M = 10**9+7
MAX_N = 200


def _pows2(n):
    pows = [1] * (n+1)
    for i in range(1,n+1):
        pows[i] = (pows[i-1] * 2) % M

    return tuple(pows)

pows2 = _pows2(MAX_N)


def pow2(n):
    return pows2[n]


def _factorials(n):
    factorials = [1] * (n+1)
    for i in range(2, len(factorials)):
        factorials[i] = (factorials[i-1] * i) % M

    return tuple(factorials)

factorials = _factorials(MAX_N)


def fact(x):
    return factorials[x]


def inv(x):
    return pow(x, M-2, M)


def _binom(n, k):
    return (fact(n) * inv(fact(k)) * inv(fact(n-k))) % M


def _binomials(n):
    binoms = [(1,)] * (n+1)
    for n in range(1,len(binoms)):
        arr = [1] * (n+1)
        for m in range(1,n):
            arr[m] = (binoms[n-1][m-1] + binoms[n-1][m]) % M

        binoms[n] = tuple(arr)
    return tuple(binoms)

binoms = _binomials(MAX_N)


def binom(n, k):
    return binoms[n][k]


def F(b, e, n, m):
    global tab

    # assert n >= 0
    # assert m >= 0
    # assert b in (0,1)
    # assert e in (0,1)

    if (b, e) == (1, 0):
        b, e = 0, 1

    be = b + e
    if m > n or be > m or n == 0 or (m == 0 and n >= 2):
        return 0

    if m == n or m <= (n - 2 + be) // 2:
        return 0

    if m == n-1:
        if n == 1:
            return 1 if be == 0 else 0

        return 0 if be == 0 else 1 if be == 1 else (pow2(n-1) - 2 + M) % M

    if m == n-2:
        if be == 0:
            return (pow2(n-1) - 2 + M) % M

    # key = (n, m, be)
    res = tab[n][m][be]
    if n <= 8 or res >= 0:
        # return tab.get(key, 0)
        return res

    assert n >= 3
    assert 1 <= m <= n-1

    # print('F', key)

    r = 0
    r0 = 0

    if be == 0:
        r = 2*(F(0, 0, n-1, m-1) + F(0, 1, n-1, m))
    elif be == 1:
        r = F(0, 1, n-1, m-1) + F(1, 1, n-1, m)
        if 2 <= m:
            r0 = F(0, 0, n-2, m-2) + F(0, 1, n-2, m-1)
    elif be == 2:
        if 3 <= m:
            r0 = 2*(F(0, 1, n-2, m-2) + F(1, 1, n-2, m-1))

    r0 %= M

    r += (r0 * (n-1)) % M
    r %= M

    # print('C', r)
    for n1 in range(2,n-2):
        n2 = n - n1 - 1
        r0 = 0
        for m1 in range(b+1, min(m,n1)+1):
            m2 = m - (m1 + 2)
            if e <= m2 <= n2:
                r1 = F(b, 0, n1, m1)
                if r1 > 0:
                    r2 = F(0, e, n2, m2)
                    if m2+1 <= n2:
                        r2 += F(1, e, n2, m2+1)

                    r0 += (r1 * r2) % M
                    r0 %= M

            if e <= m2+1 <= n2:
                r1 = F(b, 1, n1, m1)
                if r1 > 0:
                    r2 = F(0, e, n2, m2+1)
                    if m2+2 <= n2:
                        r2 += F(1, e, n2, m2+2)

                    r0 += (r1 * r2) % M
                    r0 %= M

        m2 = m - (b + 2)
        if e <= m2 <= n2:
            r1 = F(b, 0, n1, b)
            if r1 > 0:
                r2 = F(0, e, n2, m2)
                if m2 <= n2 - 1:
                    r2 += F(1, e, n2, m2+1)

                r0 += (r1 * r2) % M
                r0 %= M

        r += (r0 * binom(n-1, n1)) % M
        r %= M

    r %= M

    # tab[key] = r
    tab[n][m][be] = r
    # print('F', key, ':', r)

    return r


def G(n, m):
    r = F(0, 0, n, m)
    r += 2*F(0, 1, n, m)
    r = r % M
    r += F(1, 1, n, m)
    r = r % M
    return r


def init():
    tab = [[[-1,-1,-1] for _ in range(n+1)] for n in range(201)]
    for n in range(9):
        for m in range(n+1):
            tab[n][m][0] = 0
            tab[n][m][1] = 0
            tab[n][m][2] = 0

    # tab = {}
    for n in range(2,9):
        # print(n)
        for a in itertools.permutations(range(n)):
            b = 1 if a[0] < a[1] else 0
            e = 1 if a[-1] < a[-2] else 0
            m = 0
            for i in range(0, n):
                if i == 0:
                    if a[0] < a[1]:
                        m += 1
                elif i == n-1:
                    if a[n-1] < a[n-2]:
                        m += 1
                else:
                    if a[i] < a[i-1] or a[i] < a[i+1]:
                        m += 1

            if (b,e)!=(0,1):
                # key = (n, m, b+e)
                # tab[key] = tab.get(key, 0) + 1
                be = b + e
                tab[n][m][be] = (tab[n][m][be] + 1) % M

                # key = (n, m)
                # tab[key] = tab.get(key, 0) + 1

    # tab[(1, 1)] = 0
    # tab[(1, 0)] = 1
    # tab[(1, 0, 0)] = 1
    tab[1][0][0] = 1

    #print(tab)
    return tab

tab = init()


def query0(n, k):
    r = 0
    for m in range(k, n):
        r = (r + G(n, m)) % M

    return r

def query1(n, k):
    r = 0
    for m in range(0, k):
        r = (r + G(n, m)) % M

    return (fact(n) + M - r) % M

def query(n, k):
    if k <= n * 7 // 10:
        return query1(n, k)

    return query0(n, k)

if 0:
    for n in range(1,12):
        for m in range(1,n+1):
            print(n, m, query0(n, m), F(0, 0, n, m), F(0, 1, n, m), F(1, 1, n, m), fact(n))
        # print(F(0, 1, 4, 2))
        # print("hi")
    sys.exit(0)

if 0:
    for n in range(1,12):
        for m in range(1,n+1):
            r = query0(n, m)
            r1 = query1(n, m)
            if r != r1:
                print(n, m, r, r1, fact(n))

    sys.exit(0)

if 1:
    n,m = 100, 70
    r = query(n, m)
    print(n, m, r)
    sys.exit(0)

if 0:
    n,m = 3000, 1510
    r = query(n, m)
    print(n, m, r)
    sys.exit(0)

q = int(input().strip())
for a0 in range(q):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    # Find the number of ways to arrange 'n' people such that at least 'k' of them will be happy
    # The return value must be modulo 10^9 + 7
    result = query(n, k)
    print(result)
