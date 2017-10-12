#!/bin/python3

import sys
import bisect

MAX_T = 10**9 + 1

def preprocess1(n, t, p):
    global soonest_times, soonest_prices, soonest
    soonest = {}
    for i in range(n):
        ti = t[i]
        pi = p[i]
        soonest[pi] = min(ti, soonest.get(pi, MAX_T))

    soonest_prices = list(soonest.keys())
    soonest_prices.sort()
    m = len(soonest_prices)
    soonest_times = [MAX_T] * (m + 1)
    for i in range(m-1, -1, -1):
        price = soonest_prices[i]
        soonest_times[i] = min(soonest[price], soonest_times[i+1])

def query1(price):
    i = bisect.bisect_left(soonest_prices, price)
    time = soonest_times[i]
    return time if time < MAX_T else -1

def preprocess2(n, t, p):
    global max_prices, times, prices
    prices = {}
    for i in range(n):
        ti = t[i]
        pi = p[i]
        prices[ti] = max(pi, prices.get(ti, 0))
        
    times = list(prices.keys())
    times.sort()
    m = len(times)
    max_prices = [0] * (m + 1)
    for i in range(m-1, -1, -1):
        time = times[i]
        price = prices[time]
        max_prices[i] = max(price, max_prices[i+1])

def query2(time):
    i = bisect.bisect_left(times, time)
    price = max_prices[i]
    return price if price > 0 else -1

if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    t = tuple(map(int, input().strip().split(' ')))
    p = tuple(map(int, input().strip().split(' ')))
    preprocess1(n, t, p)
    preprocess2(n, t, p)
    for a0 in range(q):
        _type, v = input().strip().split(' ')
        _type, v = [int(_type), int(v)]
        if _type == 1:
            res = query1(v)
        else:
            res = query2(v)
            
        print(res)

