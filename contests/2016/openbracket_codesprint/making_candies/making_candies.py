
import collections
import time

# max (m + x)(w + r - x)
# mw + mr - mx + xw +xr -x^2
#-m+w+r-2x=0
#x = (w+r-m)/2
#r - x = (r-w+m)/2
# 0<=r+w-m<=2r
# 0<=r-w+m<=2r
# max = (w+r+m)**2/4

def f(N, m, w):
    global p, start
    
    if N == 0:
        return 0
    
    made = m * w
    if N <= made:
        return 1
    
    if m > w:
        m, w = w, m
    
    r = (N + w*m - 1) // (w*m)
    
    steps = 0
    n = 0
    while True:
        n += w * m
        steps += 1
        
        if n >= N:
            break

        if steps >= r:
            break

        r1 = (N - n + w*m - 1) // (w*m) + steps
        r = min(r, r1)

        if steps % 100000 == 0:
            delta = time.time() - start
            if delta > 3.96:
                break
                
        extra = n // p
        
        if extra == 0:
            dsteps = (min(N,p) - n + w*m-1) // (w*m)
            steps += dsteps
            n += dsteps * w * m
            extra = n//p
           
        if n >= N:
            break
            
        pay = extra * p
        
        if m < w:
            dm = min(w-m, extra)
            extra -= dm
            m += dm

        if m == w:
            dm = extra // 2
            m += dm
            w += dm
            extra -= 2*dm

        if extra > 0:
            w += extra

        n -= pay
        
    return min(r, steps)
    

class Task:
    def __init__(self, m, w, n, steps):
        self.m = m
        self.w = w
        self.n = n
        self.steps = steps

def g(n, m, w):
    global p, tab
    
    if n == 0:
        return 0
    
    made = m * w
    if n <= made:
        return 1

    res = (n+m*w-1) // (m*w)
    que = collections.deque()
    que.append(Task(m, w, 0, 0))
    while que:
        t = que.popleft()
        t0 = Task(t.m, t.w, t.n+t.m*t.w, t.steps+1)
        if t0.n < n:
            if t0.steps+1 < res:
                que.append(t0)
        else:
            res = min(res, t0.steps)
            break
            
        if t.m <= t.w:
            t0 = Task(t.m+1, t.w, t.n+t.m*t.w-p, t.steps+1)
        else:
            t0 = Task(t.m, t.w+1, t.n+t.m*t.w-p, t.steps+1)

        if t0.n < n:
            if t0.steps+1 < res:
                que.append(t0)
        else:
            res = min(res, t0.steps)
            break

    return res
    
    

def h(n, m, w):
    global p, tab
    
    if n == 0:
        return 0
    
    made = m * w
    if n <= made:
        return 1

    if m > w:
        m, w = w, m

    res = (n+m*w-1) // (m*w)
    que = collections.deque()
    que.append((m, w, 0, 0))
    while que:
        t = que.popleft()
        t0 = (t[0], t[1], t[2]+t[0]*t[1], t[3]+1)
        if t0[2] < n:
            if t0[3]+1 < res:
                que.append(t0)
        else:
            res = min(res, t0[3])
            break
            
        if t[0] < t[1]:
            t0 = (t[0]+1, t[1], t[2]+t[0]*t[1]-p, t[3]+1)
            
            if t0[2] < n:
                if t0[3]+1 < res:
                    que.append(t0)
            else:
                res = min(res, t0[3])
                break
                        
        t0 = (t[0], t[1]+1, t[2]+t[0]*t[1]-p, t[3]+1)
            
        if t0[2] < n:
            if t0[3]+1 < res:
                que.append(t0)
        else:
            res = min(res, t0[3])
            break

    return res



def r(n, m, w):
    global p, tab
    
    if n == 0:
        return 0
    
    made = m * w
    if n <= made:
        return 1

    if m > w:
        m, w = w, m

    res = (n+m*w-1) // (m*w)
    for i in range(1, res+1):
        n -= m*w
        if n <= 0:
            res = min(res, i)
            break
            
        n += p
        if m < w:
            m += 1
        else:
            w += 1
            
        res1 = (n+m*w-1) // (m*w)
        res = min(res, i + res1)
        
    return res

start = time.time()

m, w, p, n = [int(w) for w in input().split()]

tab = {}

steps = f(n, m, w)

print(steps)

