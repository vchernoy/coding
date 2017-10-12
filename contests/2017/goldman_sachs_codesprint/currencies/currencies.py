#!/bin/python3

import sys
import math

M = 10**9 + 7

def Gcd(n, A):
    elems = set()
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                elems.add(A[i][j])

    if len(elems) == 0:
        return 1
    
    gcd = 0
    for e in elems:
        gcd = math.gcd(gcd, e)

    if gcd > 1:
        for i in range(n):
            for j in range(n):
                A[i][j] //= gcd

    return gcd

def Mul(n, B, A, C):
    for i in range(n):
        for k in range(n):
            cik = 0
            for j in range(n):
                cik = max(cik, B[i][j] * A[j][k])

            C[i][k] = cik    

def Pow(n, m, A):
    B = A
    D = [[0]*n for _ in range(n)]
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        C[i][i] = 1

    expB = 1
    expC = 1

    while m > 0:
        if m % 2 == 1:
            Mul(n, C, B, D)
            C, D = D, C
            expC = expC * expB * Gcd(n, C)
            expC = expC % M

        m //= 2
        if m > 0:
            Mul(n, B, B, D)
            B, D = D, B
            expB = expB**2 * Gcd(n, B)
            expB = expB % M
        
    return C, expC

def currencies(n, x, s, f, m, A):
    B, exp = Pow(n, m, A)
    return (x * B[s][f] * exp) % M

if __name__ == "__main__":
    n = int(input().strip())
    x, s, f, m = input().strip().split(' ')
    x, s, f, m = [int(x), int(s), int(f), int(m)]
    A = []
    for _ in range(n):
       v = [int(e) for e in input().strip().split(' ')]
       A.append(v)
    
    res = currencies(n, x, s, f, m, A)
    print(res)

