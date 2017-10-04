
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections  

def solve(A, N):
    assert len(A) == (2*N - 1)

    H = 1
    x = N
    while x > 1:
        assert x % 2 == 0
        H += 1
        x /= 2

    levels = [None] * H

    d = {}
    for x in A:
        d[x] = d.get(x, 0) + 1

    for h in range(H-1, -1, -1):
        n = 2**h
        elems = [x for x in d.keys()]

        if len(elems) != n:
            return None

        elems.sort()

        if d[elems[0]] != h+1:
            return None

        levels[h] = elems

        for e in elems:
            d[e] = d[e] - 1
            assert d[e] >= 0
            if d[e] == 0:
                del d[e]

    for h in range(1, H):
        n = 2**h

        pset = set(levels[h-1])
        cset = set(levels[h])
        dset = cset - pset
        assert len(dset) == len(pset)
        assert len(cset) == n
        assert len(pset) * 2 == n

        delems = [e for e in dset]
        delems.sort()

        elems = [0] * n
        start = 0
        pelems = levels[h-1]
        for i in range(n//2):
            le = pelems[i]
            if (i > 0) and (le < pelems[i-1]):
                start = 0

            maybe = remove_min(le, delems, start)
            if maybe == None:
                return None
            
            j, re = maybe
            delems[j] = None
            #delems = delems[:j] + delems[j+1:]
            start = j+1
            
            elems[2*i] = le
            elems[2*i+1] = re

        levels[h] = elems

    T = []
    for h in range(H):
        T += levels[h]

    return T

def remove_min(val, arr, start=None):
    if start == None:
        start = 0
    for i in range(start, len(arr)):
        if arr[i] != None:
            if arr[i] > val:
                return (i, arr[i])

    return None

N = int(input())
A = [int(w) for w in input().split()]

sol = solve(A, N)
if sol:
    print ('YES')
    print (' '.join([str(x) for x in sol]))
else:
    print ('NO')



