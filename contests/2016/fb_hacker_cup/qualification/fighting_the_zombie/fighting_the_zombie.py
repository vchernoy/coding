#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput

fd = {}

def F(n, m, L):
    if L <= 0:
        return G(n, m)

    if n == 0:
        return 0

    key = (n,m,L)
    if key in fd:
        return fd[key]

    r = 0
    for k in range(1, m+1):
        r += F(n-1, m, L-k)

    fd[key] = r
    return r

def G(n, m):
    return m**n

def P(x, y, z, h):
    return F(x, y, h-z) / G(x, y)


f = fileinput.input()

t = int(f.readline())
for i in range(t):
    h, s = [int(w) for w in f.readline().split()]
    spells = [w for w in f.readline().split()]
    assert(len(spells) == s)
    maxp = 0
    for spell in spells:
        if '+' in spell:
            xdy, z = spell.split('+')
            z = int(z)
        elif '-' in spell:
            xdy, z = spell.split('-')
            z = -int(z)
        else:
            xdy = spell
            z = 0

        x, y = xdy.split('d')
        x = int(x)
        y = int(y)
        p = P(x, y, z, h)
        maxp = max(maxp, p)
        if maxp >= 1:
            break

    print('Case #{}: {:0.6f}'.format(i+1, maxp))

