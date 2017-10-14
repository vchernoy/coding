
def F(n, cu, cd):
    if n == 0:
        return not cu and not cd

    if cu and u[n-1]:
        return False

    if cd and d[n-1]:
        return False

    cu = cu or u[n-1]
    cd = cd or d[n-1]
    
    k = (n, cu, cd)
    if k in tab:
        return tab[k]
    
   
    if cu and cd:
        r = F(n-1, False, False)
    elif cu and not cd:
        r = F(n-1, False, True)
    elif not cu and cd:
        r = F(n-1, False, True) or F(n-1, True, False)
    else:
        r = F(n-1, False, False) or F(n-1, True, True)
    
    tab[k] = r
    return r

for _ in range(int(input())):
    n = int(input())
    u = [c == '1' for c in input()]
    d = [c == '1' for c in input()]
    
    tab = {}
    r = F(n, False, False)
    print('YES' if r else 'NO')

