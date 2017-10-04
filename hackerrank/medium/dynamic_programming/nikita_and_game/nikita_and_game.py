import sys
import bisect

def f(beg, end):
    global a, s, tab

    if beg + 1 >= end:
        return 0

    s0 = s[end] - s[beg]
    if s0 % 2 == 1:
        return 0

    r_limit = end - beg - 1
    if s0 == 0:
        return r_limit

    while (beg < end) and (a[beg] == 0):
        beg += 1

    while (beg < end) and (a[end-1] == 0):
        end -= 1

    r_limit = end - beg - 1

    k = (beg, end)
    if k in tab:
        return tab[k]

    r = 0
    s1 = s0 // 2

    x = s[beg] + s1
    i = bisect.bisect_left(s, x, beg, end)
    if i == beg:
        i += 1

    while i < end:
        s2 = s[i] - s[beg]
        if s2 == s1:
            if i - beg > r:
                r1 = f(beg, i) + 1
                r = max(r, r1)
                if r >= r_limit:
                    break
            if end - i > r:
                r1 = f(i, end) + 1
                r = max(r, r1)
                if r >= r_limit:
                    break
        else:
            break

        i += 1

    tab[k] = r

    return r

for q in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline()

    a = [int(w) for w in line.split()]

    s = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + a[i-1]

    tab = {}
    r = f(0, n)
    print(r)

