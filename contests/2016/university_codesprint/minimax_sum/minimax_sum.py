#!/bin/python

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

arr = [a,b,c,d,e]
s = sum(arr)
part_sum = [s - x for x in arr]
print(min(part_sum), max(part_sum))

