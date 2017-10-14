
def nChanges(S, c):
    n = len(c)
    f = [[1] + [0]*S]
    for i in xrange(1,n+1):
        f.append([1])
        for s in xrange(1,S+1):
            num = f[i][s-c[i-1]] if s >= c[i-1] else 0
            f[i].append(f[i-1][s] + num)

    return f[n][S]

s, n = map(int, raw_input().split())
c = map(int, raw_input().split())
print nChanges(s, c)

