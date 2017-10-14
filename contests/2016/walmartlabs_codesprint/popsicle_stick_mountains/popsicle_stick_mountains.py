
M = 10**9 + 7

def F(n, y):
    global DF

    if (n == 0) and (y > 0):
        return 0

    if (y == 0) and (n == 0):
        return 1
   
    if y > n:
        return 0

    if y == n:
        return 1

    k = (n, y)
    if k in DF:
        return DF[k]
    
    a = F(n-1, y+1)
    b = 0
    if y > 0:
        b = F(n-1, y-1)
    c = (a + b) % M
    
    if n < 2000:
        DF[k] = c
        
    return c


T = int(input())

DF = {}

Narr = []
for _ in range(T):
    N = int(input())
    Narr.append(N)

Nset = set(Narr)
Nsorted = sorted([x for x in Nset])
Nmax = Nsorted[-1]
Nres = {n:0 for n in Nset}

TF = [[0] * (Nmax+1) for _ in range(Nmax+1)]

TF[0][0] = 1
for n in range(1, Nmax+1):
    TF[n][0] = TF[n-1][1]
    for y in range(1, n):
        TF[n][y] = (TF[n-1][y+1] + TF[n-1][y-1]) % M
        
    TF[n][n] = 1


for N in Nsorted:
    r = 0
    for n in range(2, N+1, 2):
        r = (r + TF[n][0]) % M

    Nres[N] = r

for N in Narr:
    r = Nres[N]
    print(r)
    
# 900: 566396802 

