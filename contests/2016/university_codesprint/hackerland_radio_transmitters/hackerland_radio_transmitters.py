#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()

count = 0
first = x[0]
covered = 0
i = 1
while i < n:
    if first + k < x[i]:
        covered = x[i-1] + k
        count += 1
        while (i < n) and (x[i] <= covered):
            i += 1
            
        if i < n:
            first = x[i]
    else:
        i += 1

if x[-1] > covered:
    count += 1

print(count)

