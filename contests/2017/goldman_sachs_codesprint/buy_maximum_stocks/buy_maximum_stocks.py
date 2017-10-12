#!/bin/python3

import sys

def buyMaximumProducts(n, k, a):
    b = [(a[i], i+1) for i in range(n)]
    b.sort()
    counter = 0
    i = 0
    while i < n:
        p, c = b[i]
        if p > k:
            break
        max_c = min(c, k // p)
        counter += max_c
        k -= max_c * p
        i += 1

    return counter

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)


