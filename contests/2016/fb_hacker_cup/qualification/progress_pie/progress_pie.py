#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput, math


def test(x, y, p):
    if p == 0:
        return False

    r2 = x*x + y*y
    if r2 > 50*50:
        return False

    x, y = y, x

    phi = math.atan2(y, x)
    if phi < 0:
        phi += 2 * math.pi

    pphi = 100 * phi  / (2 * math.pi)
    if pphi > p:
        return False

    return True

f = fileinput.input()

t = int(f.readline())
for i in range(t):
    p, x, y = [int(w) for w in f.readline().split()]

    #print(p, x, y)
    x -= 50
    y -= 50

    res = test(x, y, p)
    if res:
        print('Case #{}: black'.format(i+1))
    else:
        print('Case #{}: white'.format(i+1))


