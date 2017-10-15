
def F(n):
    global FT

    assert(n > 0)

    won = FT.get(n, None)
    if won == None:
        won = False
        for i in xrange(1, n/2 + 1):
            if not (F(i) or F(n-1)):
                won = True
                break

        FT[n] = won

    return won;

FT = {}
for t in xrange(int(raw_input())):
    n1, n2 = [int(w) for w in raw_input().split()]
    if n1 > n2:
        n1, n2 = n2, n1

    for i in xrange(1, n2):
        F(i)

    print "Alice" if F(n1) or F(n2) else "Bob"
