
def closestSum(k, a):
    n = len(a)
    f = [([0] * (k+1)) for i in xrange(n+1)]
    
    for i in xrange(1, n+1):
        for j in xrange(1, k+1):
            val = f[i-1][j]
            if a[i-1] <= j:
                val = max(val, f[i][j-a[i-1]] + a[i-1])
            f[i][j] = val
            
    return f[n][k] 

for t in xrange(int(raw_input())):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    print closestSum(k, a)

