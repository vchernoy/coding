
def seq(a):
    n = len(a)
    g = [0]
    for i in xrange(1, n+1):
        g.append(max(0, g[i-1]+a[i-1]))

    f = [0]
    for i in xrange(1, n+1):
        f.append(max(g[i-1]+a[i-1], f[i-1]))
   
    return f[n]
    
def nonSeq(a):
    n = len(a)
    f = [0]
    for i in xrange(1, n+1):
        f.append(max(f[i-1]+a[i-1], f[i-1]))
    
    return f[n]

nTests = int(raw_input()) 
for t in xrange(nTests):
    n = int(raw_input())
    a = map(int, raw_input().split())
    maxA = max(a)
    if maxA <= 0:
        print maxA, maxA
    else:
        print seq(a), nonSeq(a)

