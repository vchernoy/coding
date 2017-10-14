
def Func(a):
    n = len(a)
    if n == 1:
        return \
            a[0] == 1 or a[0] >= 3
    
    if n == 2:
        return \
            ((a[1] - a[0] + 1) % 2 == 0) or \
            (a[0] == 2 and a[1] >= 3)
    
    if n == 3:
        return \
            (a[0] == 1) and ((a[1] == 1 and a[2] != 2) or (a[1] == 2 and a[2] % 2 == 0) or (a[1] >= 3)) or \
            (a[0] == 2) and ((a[1] == 2 and a[2] >= 3) or (a[1] >= 3 and (a[2] - a[1] + 1) % 2 == 0)) or \
            (a[0] >= 3)


    k = tuple(a)
    if k in win_tab:
        return True
    if k in lose_tab:
        return False

    win = False
    for i in range(n):
        if (a[i] >= 3) or (a[i] == 1):
            b = a[:i] + a[i+1:]
            ok = Func(b)
            if not ok:
                win = True
                break
    
    if not win:
        b = a
        for i in range(n):
            if b[i] >= 2:
                b[i] -= 1
                not_sorted = i > 0 and b[i-1] > b[i]
                if not_sorted:
                    x = b[i]
                    j = i
                    while j > 0 and b[j-1] > x:
                        b[j] = b[j-1]
                        j -= 1
                    b[j] = x
                ok = Func(b)
                if not_sorted:
                    while j < i:
                        b[j] = b[j+1]
                        j += 1
                    b[i] = x

                b[i] += 1

                if not ok:
                    win = True
                    break
                    

    if n > 3 and n < 11:
        if win:
            win_tab.add(k)
        else:
            lose_tab.add(k)
    return win

win_tab = set()
lose_tab = set()
if 1:
    for _ in range(int(input())):
        n = int(input())
        a = []
        for i in range(n):
            m, k = [int(w) for w in input().split()]
            if m > 0:
                a.append(m)
        a.sort()            

        M = sum(a)
        ok = Func(a)
        print('BOB' if ok else 'BEN')

