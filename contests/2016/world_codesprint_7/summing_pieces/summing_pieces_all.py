# Enter your code here. Read input from STDIN. Print output to STDOUT

M = 10**9 + 7

#n = int(raw_input())
#A = [int(w) for w in raw_input().split()]

n = 3
A = [1,3,6]

n = 5
A = [4, 2, 9, 10, 1]

S = [0] * (n+1)
for i in xrange(n):
    S[i+1] = (S[i] + A[i]) % M

def sm(i, j):
    assert i >= 0
    assert j >= i
    return (M + S[j] - S[i]) % M

def vol(i, j):
    assert i >= 0
    assert j >= i
    return (sm(i, j) * (j - i)) % M

T = [0] * (n+1)
T[0] = 1
T[1] = 1
for i in xrange(2, n+1):
    T[i] = (2 * T[i-1]) % M

def pow2(k):
    assert k >= 0
    if k == 0:
        return 1

    return T[k+1]

S2 = [0] * (n + 1)
S2[1] = sm(0, 1)
for i in xrange(2, n+1):
    S2[i] = (S2[i-1] + (pow2(i-2) * sm(0,i-1)) % M) % M


w = 0
S3 = [0] * (n+1)
for i in xrange(1, n+1):
    S3[i] = S3[i-1] + sm(0, i) * pow2(i-1)

print S2
print S3
print '----'

S2 = S3


T2 = [0] * (n + 1)
T2[1] = 1
for i in xrange(2, n+1):
    T2[i] = (T2[i-1] + (i * pow2(i-1)) % M ) %M

def compute0():
    B = [0] * (n+1)
    for i in xrange(1, n+1):
        b = 0
        for k in xrange(1, i+1):
            s = sm(i-k, i)
            b = (b + ((s * k) % M * T[i-k]) % M + B[i-k]) % M

        B[i] = b

    print B

    return B[n]

def compute1():
    B = [0] * (n+1)
    for i in xrange(1, n+1):
        b = vol(0, i)
        for j in xrange(1, i):
            b += B[j] + vol(j, i) * pow2(j-1)

        B[i] = b % M

    print B
    return B[n]

def compute2():
    B = [0] * (n+1)
    for i in xrange(1, n+1):
        b = 2 * B[i-1] + vol(0, i) - vol(0, i-1) + r(i)

        B[i] = b % M

    print B
    return B[n]

def r0(n):
    if n <= 0:
        return 0

    res = 0
    for i in xrange(1, n):
        res += (vol(i, n) - vol(i, n-1)) * pow2(i-1)

    return res % M

def r(n):
    if n <= 0:
        return 0

    res = 0
    #for i in xrange(1, n):
    #    res += ((n - i - 1) * A[n-1] + sm(i, n)) * pow2(i-1)

    res += (n - 1) * A[n-1] * (pow2(n-1) - 1)

    y = 0
    for i in xrange(1, n):
        y += i * pow2(i-1)

    y = T2[n-1]

    res += -y * A[n-1]

    # for i in xrange(1, n):
    #     res += sm(i, n) * pow2(i-1)

    z = sm(0, n) * (pow2(n-1) - 1)

    w = 0
    for i in xrange(1, n):
        w += sm(0, i) * pow2(i-1)

    w = S2[n-1]

    res += z - w
    return res % M


def compute3():
    B = [0] * (n+1)
    for i in xrange(1, n+1):
        b = 2 * B[i-1] + vol(0, i) - vol(0, i-1) + r1(i)

        B[i] = b % M

    print B
    return B[n]

def r1(n):
    if n <= 0:
        return 0

    an = A[n-1]
    res = (n-1) * an * (pow2(n-1) - 1) - an * T2[n-1] + sm(0, n) * (pow2(n-1) - 1) - S2[n-1]

    print n, ':', (n-1) * an * (pow2(n-1) - 1), -an * T2[n-1], sm(0, n) * (pow2(n-1) - 1), - S2[n-1]

    return res % M


print compute0()

print compute1()

print compute2()

print compute3()

print
print [r0(i) for i in xrange(1, n+1)]
print [r(i) for i in xrange(1, n+1)]
print [r1(i) for i in xrange(1, n+1)]

print

print T
print [pow2(i) for i in xrange(n)]
print T2
print S2

