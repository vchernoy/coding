
def profit(p):
    n = len(p)
    maxP = [0] * n
    for i in xrange(n-2, -1, -1):
        maxP[i] = max(maxP[i+1], p[i+1])
        
    prof = 0
    for i in xrange(n-1):
        if p[i] < maxP[i]:
            prof += maxP[i] - p[i]
            
    return prof

T = int(raw_input())

for t in xrange(T):
    n = int(raw_input())
    p = map(int, raw_input().split())
    print profit(p)

