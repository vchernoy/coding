M = 10**9 + 7

inv = [1, 500000004, 166666668, 250000002, 233333335, 83333334, 23809524, 41666667, 411111114, 850000006, 469696973]

def f0(m):
    return m

def f1(m):
    return m * (m + 1) // 2

def f2(m):
    return m * (2 * m**2 + 3 * m + 1) // 6

def f3(m):
    return m**2 * (m**2 + 2 * m + 1) // 4

def f4(m):
    return m * (6 * m**4 + 15 * m**3 + 10 * m**2 - 1) // 30

def f5(m):
    return m**2 * (2 * m**4 + 6 * m**3 + 5 * m**2 - 1) // 12

def f6(m):
    return m * (6 * m**6 + 21 * m**5 + 21 * m**4 - 7 * m**2 + 1) // 42

def f7(m):
    return m**2 * (3 * m**6 + 12 * m**5 + 14 * m**4 - 7 * m**2 + 2) // 24

def f8(m):
    return m * (10 * m**8 + 45 * m**7 + 60 * m**6 - 42 * m**4 + 20 * m**2 - 3) // 90

def f9(m):
    return m**2 * (2 * m**8 + 10 * m**7 + 15 * m**6 - 14 * m**4 + 10 * m**2 - 3) // 20

def f10(m):
    return m * (6 * m**10 + 33 * m**9 + 55 * m**8 - 66 * m**6 + 66 * m**4 - 33 * m**2 + 5) // 66

def fk(k, m):
    s = 0
    for i in range(1, m+1):
        s = (s + i**k) % M
    return s
    #return sum([i**k for i in range(1,m+1)])


def g(x):
    global f, k, m
    t = m // x
    return (f(t) * x**k) % M


def G(z, s):
    global m

    if len(s) == 0:
        return 0

    if len(s) == 1:
        return g(s[0]*z)

    if False:
        if s[0] == 1:
            return g(1)

        if len(s) == 2:
            return g(s[0]) + g(s[1]) - g(s[0]*s[1])

        if len(s) == 3:
            return g(s[0]) + g(s[1]) + g(s[2]) - g(s[0]*s[1]) - g(s[0]*s[2]) - g(s[1]*s[2]) + g(s[0]*s[1]*s[2])

        if len(s) == 4:
            return g(s[0]) + g(s[1]) + g(s[2]) + g(s[3]) \
                   - g(s[0]*s[1]) - g(s[0]*s[2]) - g(s[0]*s[3]) - g(s[1]*s[2]) - g(s[1]*s[3]) - g(s[2]*s[3]) \
                   + g(s[0]*s[1]*s[2]) + g(s[0]*s[1]*s[3]) + g(s[0]*s[2]*s[3]) + g(s[1]*s[2]*s[3]) \
                   - g(s[0]*s[1]*s[2]*s[3])

    x = s[-1]
    r = M + G(z, s[0:-1]) + G(z, [x]) - G(x*z, [y for y in s[0:-1] if y*x*z <= m])

    return r % M

# m = 0
F = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
# print ([(k, F[k](m) % M - fk(k, m)) for k in range(len(F))])


#q = int(input())
q = 1
for _ in range(q):
    #n, k, m = [int(w) for w in input().split()]
    #s = [int(w) for w in input().split()]
    n, k, m = 2, 1, 40
    s = [2, 3]

    assert len(s) == n

    s.sort()
    s = [y for y in s if y <= m]

    if s and (s[0] == 1):
        print(0)
        continue

    # f = lambda x, k=k : F[k](x) % M
    def f(x, k_=k):
        return F[k_](x) % M

    # f = lambda x : fk(k, x) % M

    res = ((f(m) - G(1, s)) % M + M) % M

    print(res)

    print(G([2]), G([3]), G([2,3]), G([6]))

    print(G([4]), G([6]), G([4,6]), G([24]), G([12]))
