
M = 10**9+7
a = [int(c)-int('0') for c in input()]
n = len(a)

g = [0]*(n+1)
for i in range(1,n+1):
    g[i] = ((g[i-1] * 10) % M + a[i-1] * i) % M 

r = 0
for i in range(n+1):
    r = (r + g[i]) % M

print(r)

if 0:
    s = [0]*(n+1)
    p = [1]*(n+1)
    for i in range(1,n+1):
        s[i] = (s[i-1]*10+a[i-1]) % M
        p[i] = (p[i-1]*10) % M 
    r = 0
    for i in range(n):
        for j in range(i, n+1):
            v = M + s[j] - (s[i]*p[j-i]) % M
            r = (r + v) % M

    print(r)

