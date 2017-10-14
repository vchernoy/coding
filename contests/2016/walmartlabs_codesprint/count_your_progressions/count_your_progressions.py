
M = 10**9 + 9

def FT_compute(n, d):
    global M, A, FT

    FT[0] = 1
    for i in range(1, n+1):  
        x = FT[i-1]
        y = G(i-1, A[i-1]-d)
        z = (x + y) % M        
        FT[i] = z

def G(n, x):
    global M, GT

    if (x > 100) or (x < 1):
        return 1

    return GT[n].get(x, 1)

def GT_compute(n, d):
    global M, A, GT

    GT[0] = {}
    for i in range(1, n+1):
        GT[i] = {}
        for last in range(1, 101):
            z = G(i-1, last)
            if A[i-1] == last:
                x = G(i-1, last-d)
                z = (x + z) % M

            if z != 1:
                GT[i][last] = z

N = int(input())

A = [0] * N
for i in range(N):
    A[i] = int(input())

#print(A)

if N == 1:
    print(2)
elif N == 2:
    print(1+2+1)
elif N < 2:
    GT = [{} for _ in range(N+1)]
    FD = {}
    GT_compute(N, 1)

    r = F(N-3, 1)
    print(r)

    r = F(N-2, 1)
    print(r)

    r = F(N-1, 1)
    print(r)

    r = F(N, 1)
    print(r)
    print(GT)

else:
    difs = set()
    all = set([A[0]])
    for i in range(1, N):
        l = [x for x in all]
        for x in l:
            d = A[i] - x
            difs.add(d)
        
        all.add(A[i])
    
    GT = [{} for _ in range(N+1)]
    FT = [0] *(N+1)

    d = 2333
    GT_compute(N, d)
    FT_compute(N, d)
    T = FT[N]
    #print('T=', T)
    r = 0
    for d in difs:
        GT_compute(N, d)
        FT_compute(N, d)
        x = FT[N] - T
        #print(d, x, GT)
        r = (r + x) % M

    r = (r + T) % M
    print(r)

