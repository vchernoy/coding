
def F(a):
    last_el = 10**9+1
    no_elems = 0
    up = False
    for i in xrange(len(a)):
        if (a[i] != last_el) and (up == (a[i] > last_el)):
            no_elems += 1
            up = not up

        last_el = a[i]

    return no_elems

n = int(raw_input())
a = [int(w) for w in raw_input().split()]
assert(len(a) == n)
print F(a)

