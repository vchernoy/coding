#!/Users/slava/work/codejam2017/env/py3/bin/python


def gen_all(n):
    res = []
    for i in range(1, n+1):
        k = i
        d = 9
        ok = True
        while ok and (k > 0):
            d0 = k % 10
            ok = d0 <= d
            d = d0
            k //= 10

        if ok:
            res.append(i)

    return res


def tidy0(n):
    return gen_all(n)[-1]

if 0:
    tidy_2digits = {}
    for i in range(10, 100):
        tidy_i = gen_all(i)[-1]
        if i != tidy_i:
            # print(i, tidy_i)
            tidy_2digits[i] = tidy_i


def tidy1(n):
    digits = [int(c) for c in str(n)]
    if len(digits) <= 1:
        return n

    ok = True
    while ok:
        ok = False

        for i in range(len(digits)-1):
            d0, d1 = digits[i], digits[i+1]
            if d0 > d1:
                ok = True
                digits[i] = d0 - 1
                for j in range(i+1, len(digits)):
                    digits[j] = 9

    return int(''.join([str(d) for d in digits]))

if 0:
    for n in range(1, 10000):
        t0 = tidy0(n)
        t1 = tidy1(n)
        assert(t0 == t1)

    print("passed")


if 0:
    n = 10**18

    for test in range(100):
        dn = (n * 129) % (10**16 - 1)
        n -= dn
        tn = tidy1(n)
        print(tn)

for test in range(int(input())):
    n = int(input())
    print("Case #{}: {}".format(test+1, tidy1(n)))
    # print("Case #{}: {}".format(test+1, tidy0(n)))


# 4
# 132
# 1000
# 7
# 111111111111111110
#
#
# 111111111111111110
# 111111111111111109
#  99999999999999999
#  99999999999999999