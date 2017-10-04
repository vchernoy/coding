
def index(x, y, z, n):
    return (x-1)*(n**2) + (y-1)*n + z-1

q = int(input())
for _ in range(q):
    n = int(input())
    m = n**3
    a = [int(w) for w in input().split()]
    assert len(a) == m
    
    res = [0]*n
    counter = len([x for x in a if x == 1])    
    res[0] = counter

    t = a
    for i in range(1, n):
        counter = 0
        tt = [0]*((n-i)**3)
        m = n-i+1
        m2 = m * m
        for x in range(1,m):    
            for y in range(1,m):    
                for z in range(1,m):
                    j = index(x,y,z,m)
                    val = max(t[j], t[j+1], t[j+m], t[j+m2], t[j+1+m], t[j+1+m2], t[j+m+m2], t[j+1+m+m2])
                    
                    ind = index(x,y,z,m-1)
                    tt[ind] = val
                    if val == i+1:
                        counter += 1
                        
        res[i] = counter
        t = tt
                    
    print(' '.join([str(x) for x in res]))

