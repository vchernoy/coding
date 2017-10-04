
M = 10**9 + 7

n = int(raw_input())
A = [int(w) for w in raw_input().split()]

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

S2 = [0] * (n+1)
for i in xrange(1, n+1):
    S2[i] = S2[i-1] + sm(0, i) * pow2(i-1)

T2 = [0] * (n + 1)
T2[1] = 1
for i in xrange(2, n+1):
    T2[i] = (T2[i-1] + (i * pow2(i-1)) % M ) %M

def compute():
    B = [0] * (n+1)
    for i in xrange(1, n+1):
        b = 2 * B[i-1] + vol(0, i) - vol(0, i-1) + r(i)

        B[i] = b % M

    return B[n]

def r(n):
    if n <= 0:
        return 0

    an = A[n-1]
    res = (n-1) * an * (pow2(n-1) - 1) - an * T2[n-1] + sm(0, n) * (pow2(n-1) - 1) - S2[n-1]

    return res % M


print compute()



