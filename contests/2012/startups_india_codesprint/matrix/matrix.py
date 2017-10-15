
import time, random

def matrix_mult(A, B):
    n = len(A)
    assert(len(B) == n)
    C = [ [0 for i in xrange(n)] for j in xrange(n) ]

    for i in xrange(n):
        for j in xrange(n):
            r = 0
            for k in xrange(n):
                if A[i][k] * B[k][j]:
                    r = 1
                    break

            C[i][j] = r

    return C

def matr_equal(A, B):
    n = len(A)
    assert(len(B) == n)

    for i in xrange(n):
        for j in xrange(n):
            if A[i][j] != B[i][j]:
                return False

    return True

def matr_rows(A, I):
    n = len(A)
    R = [0 for i in xrange(n)]
    for j in xrange(n):
        for i in I:
            if A[i][j]:
                R[j] = 1
                break

    return R

def matr_columns(A, J):
    n = len(A)
    R = [0 for i in xrange(n)]
    for j in xrange(n):
        for i in J:
            if A[j][i]:
                R[j] = 1
                break

    return R

def scalar_mult(V, W):
    n = len(V)
    for i in xrange(n):
        if V[i]*W[i]:
            return 1

    return 0;

def submatr_sum(A, I, J):
    for i in I:
        for j in J:
            if A[i][j]:
                return 1

    return 0


def passed_null_check(A, B, C):
    n = len(A)
    c = random.randint(0,2)
    I = []
    J = []
    if c == 0:
        i = random.randint(0, n-1)
        J = [j for j in xrange(n) if C[i][j] == 0]
        I = [i]
    elif c == 1:
        j = random.randint(0, n-1)
        I = [i for i in xrange(n) if C[i][j] == 0]
        J = [j]

    if (c == 2) or (len(I) * len(J) == 0):
        if len(I) == 0:
            I = [random.randint(0, n-1) for i in xrange(2)]

        if len(J) == 0:
            J = [random.randint(0, n-1) for i in xrange(2)]

    V = matr_rows(A, I)
    W = matr_columns(B, J)

    return scalar_mult(V, W) == submatr_sum(C, I, J)

def check(A, B, C):
    global no_tests, test, the_end

    cur_time = time.time()
    end_time = cur_time + (the_end - cur_time) / (no_tests - test)

    while True:
        if not passed_null_check(A, B, C):
            return False

        if time.time() >= end_time:
            return True


the_end = time.time() + 15.
random.seed()

no_tests = int(raw_input())
raw_input()

for test in xrange(no_tests):
    n = int(raw_input())
    A = []
    B = []
    C = []

    for i in xrange(n):
        A.append([int(w) for w in raw_input().split()])
        assert(len(A[-1]) == n)

    assert(len(A) == n)
    raw_input()

    for i in xrange(n):
        B.append([int(w) for w in raw_input().split()])
        assert(len(B[-1]) == n)

    assert(len(B) == n)
    raw_input()

    for i in xrange(n):
        C.append([int(w) for w in raw_input().split()])
        assert(len(C[-1]) == n)

    assert(len(C) == n)
    raw_input()

    equal = matr_equal(matrix_mult(A, B), C) if n <= 250 else check(A, B, C) 
    print "yes" if equal else "no"

