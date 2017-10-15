

def F(C):
    Mod = 1000000007
    res = 1
    for i in xrange(len(C)):
        res = (res * (i - C[i] + 1)) % Mod

    return res


for t in xrange(int(raw_input())):
    n = int(raw_input())
    C = [int(w) for w in raw_input().split()]
    assert(len(C) == n)
    C.sort()
    print F(C)

