
M = 10**9 + 7

def MM(x):
    global M
    return (M + x % M) % M

inv = [1, 500000004, 166666668, 250000002, 233333335, 83333334, 23809524, 41666667, 411111114, 850000006, 469696973]

def f0(m):
    return m % M

def f1(m):
    m = m % M
    return ((m * (m + 1)) % M * 500000004) % M
#    return m * (m + 1) // 2

def f2(m):
    m = m % M
    m2 = (m * m) % M
    return ((m * (2 * m2 + 3 * m + 1)) % M * 166666668) % M
#    return m * (2 * m**2 + 3 * m + 1) // 6

def f3(m):
    m = m % M
    m2 = (m * m) % M
    return ((m2 * (m2 + 2 * m + 1)) % M * 250000002) % M
#    return m2 * (m2 + 2 * m + 1) // 4

def f4(m):
    m = m % M
    m2 = (m * m) % M
    return ((m * ((m2 * ((6 * m2 + 15 * m + 10) % M) + M - 1)) % M) % M * 233333335) % M
#    return m * (m2 * (6 * m2 + 15 * m + 10) - 1) // 30
#    return m * (6 * m**4 + 15 * m**3 + 10 * m**2 - 1) // 30

def f5(m):
    m = m % M
    m2 = (m * m) % M
    return ((m2 * ((m2 * ((2 * m2 + 6 * m + 5) % M) + M - 1)) % M) % M * 83333334) % M
#    return m2 * (m2 * (2 * m2 + 6 * m + 5) - 1) // 12
#    return m**2 * (2 * m**4 + 6 * m**3 + 5 * m**2 - 1) // 12

def f6(m):
    m = m % M
    m2 = (m * m) % M
    return ((m * ((m2 * ((m2 * ((6 * m2 + 21 * m + 21) % M) + M - 7) % M) + 1) % M) % M) * 23809524) % M
#    return m * (m2 * (m2 * (6 * m2 + 21 * m + 21) - 7) + 1) // 42
#    return m * (6 * m**6 + 21 * m**5 + 21 * m**4 - 7 * m**2 + 1) // 42

def f7(m):
    m = m % M
    m2 = (m * m) % M
    return ((m**2 * ((m2 * ((m2 * ((3 * m2 + 12 * m + 14) % M) + M - 7) % M) + 2) % M)) % M * 41666667)
#    return m**2 * (m2 * (m2 * (3 * m2 + 12 * m + 14) - 7) + 2) // 24
#    return m**2 * (3 * m**6 + 12 * m**5 + 14 * m**4 - 7 * m**2 + 2) // 24

def f8(m):
    m = m % M
    m2 = (m * m) % M
    return (MM(m * MM(m2 * MM(m2 * MM(m2 * MM(10 * m2 + 45 * m + 60) - 42) + 20) - 3)) * 411111114) % M
#    return m * (m2 * (m2 * (m2 * (10 * m2 + 45 * m + 60) - 42) + 20) - 3) // 90
#    return m * (10 * m**8 + 45 * m**7 + 60 * m**6 - 42 * m**4 + 20 * m**2 - 3) // 90

def f9(m):
    m = m % M
    m2 = (m * m) % M
    return (MM(m2 * MM(m2 * MM(m2 * MM(m2 * MM(2 * m2 + 10 * m + 15) - 14) + 10) - 3)) * 850000006) % M
#    return m2 * (m2 * (m2 * (m2 * (2 * m2 + 10 * m + 15) - 14) + 10) - 3) // 20
#    return m**2 * (2 * m**8 + 10 * m**7 + 15 * m**6 - 14 * m**4 + 10 * m**2 - 3) // 20

def f10(m):
    m = m % M
    m2 = (m * m) % M
    return (MM(m * MM(m2 * MM(m2 * MM(m2 * MM(m2 * MM(6 * m2 + 33 * m + 55) - 66) + 66) - 33) + 5)) * 469696973) % M
#    return m * (m2 * (m2 * (m2 * (m2 * (6 * m2 + 33 * m + 55) - 66) + 66) - 33) + 5) // 66
#    return m * (6 * m**10 + 33 * m**9 + 55 * m**8 - 66 * m**6 + 66 * m**4 - 33 * m**2 + 5) // 66

def p0(x):
    return 1

def p1(x):
    return x % M

def p2(x):
    _x = x % M
    return (_x *_x) % M

def p3(x):
    _x = x % M
    _x2 = (_x * _x) % M
    return (_x *_x2) % M

def p4(x):
    _x = x % M
    _x2 = (_x * _x) % M
    return (_x2 *_x2) % M

def p5(x):
    _x = x % M
    _x2 = (_x * _x) % M
    return ((_x2 *_x2) % M * _x) % M

def p6(x):
    _x3 = p3(x)
    return (_x3 * _x3) % M

def p7(x):
    _x = x % M
    _x3 = p3(_x)
    return ((_x3 * _x3) % M * _x) % M

def p8(x):
    _x4 = p4(x)
    return (_x4 * _x4) % M

def p9(x):
    _x = x % M
    _x4 = p4(_x)
    return ((_x4 * _x4) % M * _x) % M

def p10(x):
    _x = x % M
    _x2 = (_x * _x) % M
    return p5(_x2)

def pow1(x, k):
    global M
    e = x % M
    r = 1
    for _ in range(k):
        r = (r * e) % M
        
    return r

def pow0(x, k):
    global M
    e = x % M
    return (e**k) % M

def pow(x, k):
    global M
    e = x % M
    r = 1
    while k > 0:
        if k % 2 == 1:
            r = (r * e) % M

        e = (e*e) % M
        k /= 2

    return r

def g(x):
    global fk, k, m, M, pk
    t = m // x
#    return ((fk(t) % M) * x**k) % M
    return ((fk(t) % M) * pk(x)) % M

def G(z, beg, end):
    global m, s

    if beg >= end:
        return 0

    if beg + 1 == end:
        return g(s[beg]*z)

    if beg + 2 == end:
        return g(s[beg]*z) + g(s[beg+1]*z) - g(s[beg]*s[beg+1]*z)

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

    x = s[end-1]
    r = M + G(z, beg, end-1) + G(z, end-1, end)
    
    
    if x*z <= m:
        end -= 1
        while (end > beg) and (s[end-1] * x * z > m):
            end -= 1
            
        r -= G(x*z, beg, end) # G(x*z, [y for y in s[0:-1] if y*x*z <= m])

    return r % M

F = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
P = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

q = int(input())
for _ in range(q):
    n, k, m = [int(w) for w in input().split()]
    s = [int(w) for w in input().split()]
    assert len(s) == n

    fk = F[k]
    pk = P[k]
    
    s.sort()
    s = [y for y in s if y <= m]

    if s and (s[0] == 1):
        print(0)
        continue
    
    res = fk(m) % M - G(1, 0, len(s))
    res = res % M
    res += M
    res = res % M

    print (res)

