#!/Users/slava/work/codejam2017/env/py3/bin/python


def stalls(n, k):
    a = [(n,1)]
    last_n = 0
    while k > 0 and len(a) > 0:
        a.sort()
        n, c = a[-1]
        last_n = n
        k1 = min(c, k)
        c1 = c - k1
        if n % 2 == 0:

        else:

    if last_n <= 1:
        return 0, 0

    if last_n % 2 == 0:
        return last_n // 2, last_n // 2 - 1

    return last_n // 2, last_n // 2

for test in range(int(input())):
    n, k = [int(w) for w in input().split()]
    print("Case #{}: {}".format(test+1, stalls(n, k)))


