

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
s = raw_input()
abc = set(s)
all = {}
for c1 in abc:
    for c2 in abc:
        if c1 < c2:
            all[(c1,c2)] = ''
        elif c2 < c1:
            all[(c2,c1)] = ''

d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
    for (c1,c2) in all.keys():
        n1 = d.get(c1, 0)
        n2 = d.get(c2, 0)
        last = all[(c1,c2)]
        if abs(n1 - n2) > 1:
            del all[(c1,c2)]
        elif (c1 == c) or (c2 == c):
            if last == c:
                del all[(c1,c2)]
            else:
                all[(c1,c2)] = c

res = 0
for (c1,c2) in [x for x in all]:
    n1 = d.get(c1, 0)
    n2 = d.get(c2, 0)
#    if n1 != n2:
    res = max(res, (n1 + n2))

print res


