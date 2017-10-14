
# sum(0 <= i < n-1, i+1 <= j < n: Aj - Ai) = 
# sum(0 <= i < n-1: sum(i+1 <= j < n: Aj - Ai)) = 
# sum(0 <= i < n-1: sum(i+1 <= j < n: Aj) - sum(i+1 <= j < n: Ai)) = 
# sum(0 <= i < n-1: sum(i+1 <= j < n: Aj) - (n-i-1)*Ai ) = 
# sum(0 <= i < j < n: Aj) - sum(0 <= i < n-1: (n-i-1)*Ai ) = 
# sum(1 <= j < n: sum(0 <= i < j: Aj)) - sum(0 <= i < n-1: (n-i-1)*Ai ) = 
# sum(1 <= j < n: Aj*sum(0 <= i < j: 1)) - sum(0 <= i < n-1: (n-i-1)*Ai ) = 
# sum(1 <= j < n: Aj*j) - sum(0 <= i < n-1: (n-i-1)*Ai ) = 
# sum(1 <= i < n: Ai*i) - sum(0 <= i < n-1: (n-i-1)*Ai ) = 
# sum(1 <= i < n-1: Ai*i) - sum(1 <= i < n-1: (n-i-1)*Ai ) + A{n-1}*(n-1) - (n-1)A0 = 
# sum(1 <= i < n-1: Ai*i - (n-i-1)*Ai ) + A{n-1}*(n-1) - (n-1)A0 = 
# sum(1 <= i < n-1: Ai*i -n*Ai +i*Ai + Ai) + A{n-1}*(n-1) - (n-1)A0 = 
# sum(1 <= i < n-1: 2i*Ai -n*Ai + Ai) + A{n-1}*(n-1) - (n-1)A0 = 
# sum(1 <= i < n-1: 2i*Ai) - (n-1)*sum(1 <= i < n-1: Ai) + A{n-1}*(n-1) - (n-1)A0 = 
# 2*sum(1 <= i < n-1: i*Ai) - (n-1)*(S-A0-A{n-1}) + A{n-1}*(n-1) - (n-1)A0 = 
# 2*sum(1 <= i < n-1: i*Ai) - (n-1)*S +A0*(n-1)+A{n-1}*(n-1) + A{n-1}*(n-1) - (n-1)A0 = 
# 2*sum(1 <= i < n-1: i*Ai) - (n-1)*S + 2*A{n-1}*(n-1)  = 
# 2*sum(1 <= i < n: i*Ai) - (n-1)*S  = K
# 2*sum(1 <= i < n: i*Ai)  = K + (n-1)*S

A = []

def Func(n, s, t, d):
    assert n >= 0
    
    if n == 1:
        ok = t == 0
        if ok:
            A.append(s+d)
        return ok
    
    if 2*(n-1) * s < t:
        return False

    ok = False
    max_x = min(s//n, t//n//(n-1))
    for x in range(max_x+1):
        s0 = s-n*x
        t0 = t - n*(n-1)*x - 2*s0
        ok = Func(n-1, s0, t0, d+x)
        if ok:
            A.append(x+d)
            break
        
    #print('Func:', n, s, t, ok)
    return ok


for _ in range(int(input())):
    n, s, k = [int(w) for w in input().split()]
        
    A = []    
    if (k + (n-1)*s) % 2 != 0:
        print(-1)
        continue
        
    if (n-1) * s < k:
        print(-1)
        continue

    if (n-1) * s == k:
        print(' '.join([str(x) for x in ([0]*(n-1) + [s])]))
        continue
    
    if 0:
        a = [0] * n
        sp = s
        s2p = k+(n-1)*s
        print("start", s2p, s2p // 2)
        for i in range(n-1, 0, -1):
            a[i] = min(sp, s2p // 2 // i)
            a[i] = max(a[i], 0)
            if i < n-1:
                a[i] = min(a[i], a[i+1])

            sp -= a[i]
            s2p -= 2*i*a[i]
            if (sp > 0) and (s2p == 0) and (a[i] > 0):
                a[i] -= 1
                sp += 1
                s2p += 2*i
            print(i, ':', a[i], sp, s2p)

        a[0] = min(sp, a[1])
        sp -= a[0]
        print(a)    
        if (sp > 0) or (s2p > 0):
            print(-1)
        else:
            print(' '.join([str(x) for x in a]))
    
    ok = Func(n, s, k+(n-1)*s, 0)
    if ok:
        A.reverse()
        print(' '.join([str(x) for x in A]))
    else:
        print(-1)

