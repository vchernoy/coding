#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput


def rounds(w):
    w.sort()
    beg = 0
    end = len(w) - 1
    r = 0
    while beg <= end:
        n_items = end - beg + 1
        if w[end] >= 50:
            n_req_items = 1
        else:
            n_req_items = (50 + w[end] - 1) // w[end]

        if n_req_items > n_items:
            break

        r += 1
        beg += n_req_items - 1
        end -= 1

    return r


f = fileinput.input()

t = int(f.readline())
for i in range(t):
    n = int(f.readline())
    w = [0] * n
    for j in range(n):
        w[j] = int(f.readline())

    #print(i, n, w)
    r = rounds(w)
    print('Case #{}: {}'.format(i+1, r))
