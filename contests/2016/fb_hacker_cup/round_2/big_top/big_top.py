#!/usr/local/bin/pypy3

# !/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput, bintrees, sys


MX = 100000000


def generate(n, x1, h1, ax, bx, cx, ah, bh, ch):
    all_x = {x1}
    x = [None] * n
    x[0] = (x1, h1)
    xi = x1
    hi = h1
    for i in range(1, n):
        hi = ((ah * hi + bh) % ch) + 1
        xi = ((ax * xi + bx) % cx) + 1
        x[i] = (xi, hi)
        assert xi not in all_x
        all_x.add(xi)

    return x


def solve0(x):
    z = x
    x = []
    res = 0
    for k in range(len(x)):
        x.append(z[k])
        if x and (z[k][0] <= x[-1][0]):
            x.append(z[k])
            x.sort()
        else:
            x.append(z[k])
            # x.sort()

        n = len(x)

        xx = []
        i = 0
        while i < n:
            if xx:
                x_last, h_last = xx[-1]
                x_cur, h_cur = x[i]
                if covers(x_last, h_last, x_cur, h_cur):
                    i += 1
                elif covers(x_cur, h_cur, x_last, h_last):
                    xx.pop()
                else:
                    xx.append(x[i])
            else:
                xx.append(x[i])
                i += 1

        x = xx

        x_cur, h_cur = xx[0]
        square = h_cur * h_cur * 0.5
        x_last, h_last = x_cur, h_cur
        for i in range(1, len(xx)):
            x_cur, h_cur = xx[i]
            dx = x_cur - x_last
            if dx >= h_cur + h_last:
                square += (h_cur * h_cur + h_last * h_last) * 0.5
            else:
                h0 = min(h_cur, h_last)
                dh = abs(h_cur - h_last)
                square += (h_cur + h_last) * 0.5 * dh
                square += (2 * h0 - (dx - dh)*0.5) * (dx - dh) * 0.5

            x_last, h_last = x_cur, h_cur

        square += h_cur * h_cur * 0.5
        res += square

    return res


def solve1(x):
    ordered = bintrees.AVLTree()
    res = 0
    for k in range(len(x)):
        xk, hk = x[k]

        to_add = True
        x1 = xk
        for x0, h0 in ordered.item_slice(0, xk, reverse=True):
            if covers(x0, h0, xk, hk):
                to_add = False
                break
            elif covers(xk, hk, x0, h0):
                x1 = x0
                pass
            else:
                break

        x2 = xk
        for x0, h0 in ordered[xk:].items():
            if covers(x0, h0, xk, hk):
                to_add = False
                break
            elif covers(xk, hk, x0, h0):
                x2 = x0
                pass
            else:
                break

        del ordered[x1:x2+1]
        if to_add:
            ordered.insert(xk, hk)

        x_cur, h_cur = ordered.min_item()

        square = h_cur * h_cur * 0.5
        x_last, h_last = x_cur, h_cur
        for x_cur, h_cur in ordered[x_last+1:].items():
            dx = x_cur - x_last
            if dx >= h_cur + h_last:
                square += (h_cur * h_cur + h_last * h_last) * 0.5
            else:
                h0 = min(h_cur, h_last)
                dh = abs(h_cur - h_last)
                square += (h_cur + h_last) * 0.5 * dh
                square += (2 * h0 - (dx - dh)*0.5) * (dx - dh) * 0.5

            x_last, h_last = x_cur, h_cur

        square += h_cur * h_cur * 0.5
        res += square

    return res


def solve(x):
    ordered = bintrees.AVLTree()
    ordered[-MX] = (0,0)
    ordered[+MX] = (0,0)
    res = 0
    square = 0
    for k in range(len(x)):
        xk, hk = x[k]
        # print(xk, hk)

        to_add = True
        x1 = xk
        for x0, (h0, s0) in ordered.item_slice(0, xk, reverse=True):
            if covers(x0, h0, xk, hk):
                to_add = False
                break
            elif covers(xk, hk, x0, h0):
                x1 = x0
                pass
            else:
                break

        x2 = xk
        for x0, (h0, s0) in ordered[xk:].items():
            if covers(x0, h0, xk, hk):
                to_add = False
                break
            elif covers(xk, hk, x0, h0):
                x2 = x0
                pass
            else:
                break


        if x2 == xk:
            x2 = ordered.ceiling_key(x2)
        else:
            x2 = ordered.succ_key(x2)


        print('range:', x1, x2)
        s = 0
        for x0, (h0, s0) in ordered[x1:x2].items():
            s += s0

        square -= s

        del ordered[x1:x2]
        if to_add:
            ordered.insert(xk, (hk, 0))

        x1 = ordered.floor_key(x1)
        x_last, (h_last, _) = ordered.prev_item(x1)
        for x_cur, (h_cur, s_cur) in ordered[x1:x2].items():
            dx = x_cur - x_last
            s_new = shape_square(h_last, h_cur, dx)
            print('square: ', h_last, h_cur, dx, ':', s_new)
            square += -s_cur + s_new
            ordered[x_cur] = (h_cur, s_new)
            x_last, h_last = x_cur, h_cur

        print(square)
        print(ordered)
        res += square

    return res


def shape_square(h0, x1, h1):
    print(h0, x1, h1)
    assert x1 > 0
    assert h1 >= 0
    assert h0 >= 0

    if h1 > h0:
        h1, h0 = h0, h1

    if h0 + h1 >= x1:
        return (h0 * h0 + h1 * h1) * 0.5

    y0 = (h0 + h1 - x1) * 0.5
    x0 = (h0 - h1 + x1) * 0.5 # h0 - y0

    square = (x0*(h0 - h1) + x1*(h1+y0)) * 0.5
    return square





def covers(x1, h1, x2, h2):
    dx = abs(x2 - x1)
    if dx > h1:
        return False

    if h2 <= h1 - dx:
        print(x1, h1, 'covers', x2, h2, file=sys.stderr)
        sys.stderr.flush()
        return True

    return False


def main():
    f = fileinput.input()

    for test in range(int(f.readline())):
        n = int(f.readline())
        x1, ax, bx, cx = [int(w) for w in f.readline().split()]
        h1, ah, bh, ch = [int(w) for w in f.readline().split()]
        x = generate(n, x1, h1, ax, bx, cx, ah, bh, ch)
        res = solve(x)
        print('Case #{}: {}'.format(test+1, res))


# main()

# d = collections.OrderedDict({20:10, 30:15, 24:3})
# print(d)

r = solve([(20, 10), (30, 15), (24, 3)])
print(r)
#
# res = solve([(0, 4), (2, 4)])
# print(res)
#
#
# res = solve([(0, 4), (8, 4)])
# print(res)
#
# res = solve([(0, 4), (7, 4)])
# print(res)
#
# res = solve([(0, 4), (6, 4)])
# print(res)
