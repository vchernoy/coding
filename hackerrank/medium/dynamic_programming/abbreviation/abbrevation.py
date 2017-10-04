# Enter your code here. Read input from STDIN. Print output to STDOUT

def f(n, m):
    global a, b, d, tab

    if (n == 0) and (m == 0):
        return True

    if n < m:
        return False
    
    if m == 0:
        for i in range(n):
            if not d[i]:
                return False

        return True

    k = (n, m)
    if k in tab:
        return tab[k]
    
    r = (a[n-1] == b[m-1]) and f(n-1, m-1) 
    if d[n-1]:
        r = r or f(n-1, m) 

    tab[k] = r
    return r

q = int(input())
for _ in range(q):
    a = [c for c in input()]
    b = [c for c in input()]
    d = [(c >= 'a') and (c <= 'z') for c in a]
    a = [c.upper() for c in a]
    tab = {}
    r = f(len(a), len(b))
    print('YES' if r else 'NO')

