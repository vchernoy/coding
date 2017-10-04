#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput

M = 1000000007


def inv(x):
    return pow(x, M-2, M)


fact_values = [1] * 1000000000


def init_fact():
    global fact_values

    res = 1
    for i in range(2, len(fact_values)):
        res = (res * i) % M
        fact_values[i] = res


def mod_fact(x):
    global fact_values

    if x >= M:
        return 0

    return fact_values[x]


def compute1(m, r):
    n = len(r)
    s = sum(r)

    if n == 1:
        return m

    tab = {}

    res = 0
    for i in range(n):
        for j in range(i+1, n):
            min_space = 2*s - r[i] - r[j]
            extra_space = m - 1 - min_space
            if extra_space >= 0:
                res1 = tab.get(extra_space)
                if res1 is None:
                    res1 = 0
                    for es in range(extra_space+1):
                        res0 = (mod_fact(n - 2 + es) * inv(mod_fact(es))) % M
                        res0 = (res0 * (extra_space + 1 - es)) % M
                        res1 = (res1 + res0) % M

                    tab[extra_space] = res1

                res = (res + res1) % M

    res = (res * 2) % M

    return res


def compute(m, r):
    n = len(r)
    s = sum(r)

    if n == 1:
        return m

    tab = {}

    inv_n_choose_2 = inv(((n-1) * n // 2) % M)

    res = 0
    for i in range(n):
        for j in range(i+1, n):
            min_space = 2*s - r[i] - r[j]
            extra_space = m - 1 - min_space
            if extra_space >= 0:
                res1 = tab.get(extra_space)
                if res1 is None:
                    res1 = mod_fact(extra_space + n) * inv(mod_fact(extra_space))
                    res1 = res1 % M
                    tab[extra_space] = res1

                res = (res + res1) % M

    res = (res * inv_n_choose_2) % M

    return res


def main():
    f = fileinput.input()

    for test in range(int(f.readline())):
        n, m = [int(w) for w in f.readline().split()]
        r = [0] * n
        for i in range(n):
            r[i] = int(f.readline())

        res = compute(m, r) % M
        print('Case #{}: {}'.format(test+1, res))


init_fact()

main()
