#!/Users/slava/work/codejam2017/env/py3/bin/python


def solve0(n, r, o, y, g, b, v):
    assert o == 0
    assert g == 0
    assert v == 0

    a = [(r, 'R'), (y, 'Y'), (b, 'B')]
    a.sort()
    m = a[-1][0]
    if m > n // 2:
        return 'IMPOSSIBLE'

    #print(a)
    res = [a[-1][1]] * n

    i = 0
    while a[0][0] < a[1][0]:
        for j in [1,2]:
            x = a[j]
            if x[0] > 0:
                res[i] = x[1]
                i += 1
                a[j] = (x[0]-1, x[1])

    while a[1][0] < a[2][0]:
        for j in [0,2,1,2]:
            x = a[j]
            if x[0] > 0:
                res[i] = x[1]
                i += 1
                a[j] = (x[0]-1, x[1])

    while i < n:
        for j in [0,1,2]:
            x = a[j]
            if x[0] > 0:
                res[i] = x[1]
                i += 1
                a[j] = (x[0]-1, x[1])

    return ''.join(res)


def solve(n, r, o, y, g, b, v):
    b = [(r, 'R'), (y, 'Y'), (b, 'B'), (o, 'O'), (g, 'G'), (v, 'V')]
    a = {x:nx for (nx, x) in b}
    b.sort()
    x = b[-1][1]

    m = {'R': 'BYG', 'B':'RYO', 'Y':'RBV', 'O':'BGV', 'G':'ROV', 'V':'YOG'}
    res = ['']*n
    i = 0
    while i < n:
        assert x in 'RBYOGV'

        nx = a[x]
        if nx == 0:
            return 'IMPOSSIBLE'

        res[i] = x
        i += 1
        nx -= 1
        a[x] = nx

        ys = m[x]
        c = {y:a[y] for y in ys}
        d = [(c[y], y) for y in c]
        d.sort()
        x = d[-1][1]

    if n > 0 and res[0] == res[-1]:
        return 'IMPOSSIBLE'

    return ''.join(res)



def check(res):
    for i in range(len(res)):
        if res[i] == res[(i+len(res)-1) % len(res)]:
            return False

    return True


for test in range(int(input())):
    n, r, o, y, g, b, v = [int(w) for w in input().split()]
    res = solve0(n, r, o, y, g, b, v)

    print("Case #{}: {}".format(test+1, res))
    if res != 'IMPOSSIBLE':
        assert check(res)
