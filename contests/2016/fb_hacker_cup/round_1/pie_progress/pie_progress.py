#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput


def process_cost(n, m, s):
    tab = {}

    def cost(pies, i):
        if i == n:
            return 0

        days = n - i
        if pies > days:
            return 0

        key = (pies, i)
        res = tab.get(key, None)
        if res is None:
            si = s[i]
            for b in range(m+1):
                if pies > 0 or b > 0:
                    extra = si[b] # + b*b
                    if res is not None:
                        if extra >= res:
                            break

                    r = cost(pies + b - 1, i+1) + extra
                    if res is None:
                        res = r
                    else:
                        res = min(res, r)

            tab[key] = res

        return res

    return cost(0, 0)


def main():
    f = fileinput.input()

    for k in range(int(f.readline())):
        n, m = [int(w) for w in f.readline().split()]
        c = []
        for i in range(n):
            ci = [int(w) for w in f.readline().split()]
            c.append(ci)

        s = []
        for i in range(n):
            ci = c[i]
            ci.sort()
            si = [0] * (m+1)
            for b in range(1, m+1):
                si[b] = si[b-1] + ci[b-1] + 2*b-1

            s.append(si)

        res = process_cost(n, m, s)
        print('Case #{}: {}'.format(k+1, res))


main()
