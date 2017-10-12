#!/Users/slava/work/codejam2017/env/pypy3/bin/python

INF = 10**18

def is_free(t, dt):
    ok = True
    when = t
    for beg, end in dt:
        if beg <= t < end:
            ok = False
            when = min(when, beg)

    return ok, when


def set(d, k, v):
    d0 = dict(d)
    d0[k] = v
    return d0

def F(who, t, tw, tab, when):
    assert sum(tw.values()) == t
    assert t >= 0
    assert tw[True] >= 0
    assert tw[False] >= 0

    if t == 0:
        return 0

    key = (who, tw[True], tw[False])
    if key in tab:
        return tab[key]

    if tw[who] <= 0:
        return INF

    #print(t-1, dtw[who])
    when_free0 = when[who][t-1]
    when_free1 = when[not who][t-1]

    assert when_free0 == t-1

    res0 = res1 = INF

    if when_free1 == t-1:
        duration = 1
    else:
        duration = t-1 - when_free1

    duration = min(duration, tw[who])

    assert duration > 0

    if duration == tw[who]:
        assert 0 < duration
        if tw[not who] > 0:
            res1 = F(not who, t-duration, set(tw, who, 0), tab, when) + 1
        else:
            res1 = 0
    else:
        assert 0 < duration < tw[who]

        res0 = F(who, t-duration, set(tw, who, tw[who]-duration), tab, when)
        if tw[not who] > 0 and when[not who][t-duration-1] == t-duration-1:
            res1 = F(not who, t-duration, set(tw, who, tw[who]-duration), tab, when) + 1

    res = min(res0, res1)

    tab[key] = res
    return res


def when_free(dt):
    minutes = [True] * (60*24)
    for beg, end in dt:
        for t in range(beg, end):
            minutes[t] = False

    free_t = -1
    when = [-1] * (60*24)
    for t in range(60*24):
        if minutes[t]:
            free_t = t
        when[t] = free_t

    return tuple(when)


def solve(ac, aj, dtc, dtj):
    tab = {}
    dtc.sort()
    dtj.sort()
    #dtw = {True:dtc, False:dtj}
    when = {True:when_free(dtc), False:when_free(dtj)}

    print(dtc)
    print(dtj)
    #print(when[False])
    #print(when[True])

    res0 = res1 = INF
    t = 24*60
    if when[True][t-1] == t-1:
        res0 = F(True,  t, {False:t//2, True:t//2}, tab, when)

    if when[False][t-1] == t-1:
        res1 = F(False, t, {False:t//2, True:t//2}, tab, when)

    print(min(res0, res1), res0, res1)
    return min(res0, res1)


for test in range(int(input())):
    ac, aj = [int(w) for w in input().split()]
    dtc = [None] * ac
    for i in range(ac):
        b, e = [int(w) for w in input().split()]
        dtc[i] = (b, e)

    dtj = [None] * aj
    for i in range(aj):
        b, e = [int(w) for w in input().split()]
        dtj[i] = (b, e)

    res = solve(ac, aj, dtc, dtj)

    print("Case #{}: {}".format(test+1, res))




