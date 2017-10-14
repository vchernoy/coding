
M = 10**9 + 7

# F(10**14) = 264301918 
def Fib(n):
    global M, FT
    
    if n <= 1:
        return n
    
    #if (n < len(FT)) and (FT[n] >= 0):
    #    return FT[n]
    if n in FT:
        return FT[n]
    
    k = (n+1)//2
    fk = Fib(k)
    fk1 = Fib(k-1)
    if n % 2 == 0:
        r = ((2*fk1 + fk) % M * fk) % M
    else:
        r = ((fk*fk)%M + (fk1*fk1)%M) % M

    #if n < len(FT):
    #    FT[n] = r
    FT[n] = r 
    return r

def Sum(L, R):
    return S[R] - S[L]

def Do():
    global A, S, N, M
    
    r = 0
    for L in range(N):
        for R in range(L, N+1):
            #s = S[R] - S[L]
            #Fs = Fib(s)
            
            Fs = ((FS[R] * FS1[L]) % M - (FS1[R] * FS[L]) % M) % M
            if S[L] % 2 == 1:
                Fs = (Fs * (M-1)) % M

            #if Fs != Fs2:
            #    print('!', Fs, Fs2)
            r = (r + Fs) % M
            
    return r

#FT = [-1] * (6*10**7)
FT = {}

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = [int(w) for w in input().split()]
    assert len(A) == N
    
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i-1]
        
    FS = [0] * (N+1)
    FS1 = [0] * (N+1)
    for i in range(0, N+1):
        FS[i] = Fib(S[i])
        FS1[i] = Fib(S[i]+1)

    r = Do()
    print(r)

