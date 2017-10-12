#!/bin/python3

import sys

def F(k, n, A, tab):
    if k == 0:
        return 0
    if n <= 1:
        return 0
    
    key = (k, n)
    profit = tab.get(key)
    if profit is not None:
        return profit

    profit = 0
    max_p = A[n-1]
    j = n-2
    while j >= 0:
        if A[j] < max_p:
            profit_j = max_p - A[j] + F(k-1, j, A, tab)
            profit = max(profit, profit_j)
        max_p = max(max_p, A[j])
        j -= 1
        
    tab[key] = profit
    return profit

def traderProfit(k, n, A):
    return F(k, n, A, {})

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        k = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = traderProfit(k, n, arr)
        print(result)


