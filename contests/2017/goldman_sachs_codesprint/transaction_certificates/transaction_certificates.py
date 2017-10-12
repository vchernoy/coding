import random

def compute_power_p(n):
    global m, p
    arr = [0] * n
    arr[0] = 1
    for i in range(1, n):
        arr[i] = (arr[i-1] * p) % m

    return tuple(arr)

def rand_gen_da(n):
    global p_powers, k

    tab = {}
    tab1 = {}
    da = [0] * n
    c = 0
    n_zeros = n
    while True:
        ai = random.randint(-(k-1), k-1)
        i = random.randint(0, n-1)

        if da[i] == 0:
            n_zeros -= 1

        dai = (m + (ai - da[i]) % m) % m
        c = (c + dai * p_powers[i]) % m

        da[i] = ai

        if da[i] == 0:
            n_zeros += 1

        if n_zeros < n:
            if c == 0:
                return da

            tda = None
            if c not in tab:
                tda = tuple(da)
                tab[c] = tda

            pnc = (p_powers[n] * c) % m
            # c0 + p**n * c == 0 ???
            c0 = (m - pnc) % m
            if c0 in tab:
                res = list(tab[c0])
                res.extend(da)
                return res

            if pnc not in tab1:
                tda = tda or tuple(da)
                tab1[pnc] = tda

            pnc1 = (m - c) % m
            if pnc1 in tab1:
                res = list(da)
                res.extend(tab1[pnc1])
                return res

    assert False

if __name__ == "__main__":
    n, k, p, m = input().strip().split(' ')
    n, k, p, m = [int(n), int(k), int(p), int(m)]
    p_powers = compute_power_p(n+1)

    da = rand_gen_da(n)
    n = len(da)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        dai = da[i]
        if dai >= 0:
            a[i] = 1
            b[i] = 1 + dai
        else:
            a[i] = k
            b[i] = k + dai

    a.reverse()
    b.reverse()

    print(' '.join([str(x) for x in a]))
    print(' '.join([str(x) for x in b]))

