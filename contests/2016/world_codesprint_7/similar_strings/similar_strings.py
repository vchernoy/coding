

# Enter your code here. Read input from STDIN. Print output to STDOUT

from operator import itemgetter, attrgetter, methodcaller


def check0(s1, s2):
    ds1 = [-1] * 10 #{c:-1 for c in 'abcdefghij'}
    ds2 = [-1] * 10 #{c:-1 for c in 'abcdefghij'}
    for j in xrange(m):
        c1 = ord(s1[j]) - ord('a')
        c2 = ord(s2[j]) - ord('a')

        if ds1[c1] == ds2[c2]:
            ds1[c1] = j
            ds2[c2] = j
        else:
            return False

    return True

def check1(s1, s2):
    mapping1 = [None] * 10
    mapping2 = [None] * 10
    for j in xrange(m):
        c1 = ord(s1[j]) - ord('a')
        c2 = ord(s2[j]) - ord('a')

        c21 = mapping1[c2]
        c12 = mapping2[c1]
        if (c21 == None) and (c12 == None):
            mapping1[c2] = c1
            mapping2[c1] = c2
        elif (c21 != c1) or (c12 != c2):
            return False

    #print s1, s2, mapping1, mapping2

    return True

def hash_val(vals):
    h = len(vals)
    for x in vals:
        h = h * 31 + x

    return h

def check(ds1, ds2, set1):
    if len(ds1) != len(ds2):
        return False

    fp1 = [len(l1) for l1 in ds1.itervalues()]
    fp2 = [len(l2) for l2 in ds2.itervalues()]
    fp1.sort()
    fp2.sort()
    if fp1 != fp2:
        return False

    fp1 = [hash_val(l1) for l1 in ds1.itervalues()]
    fp2 = [hash_val(l2) for l2 in ds2.itervalues()]
    #fp1.sort(key=itemgetter(0,1))
    #fp2.sort(key=itemgetter(0,1))
    fp1.sort()
    fp2.sort()
    if fp1 != fp2:
        return False

    return True

    set2 = set(','.join([str(x) for x in l2]) for l2 in ds2.itervalues())

    return set1 == set2

N, NQ = [int(w) for w in raw_input().split()]
S = raw_input()

Q = []
for i in xrange(NQ):
    l, r = [int(w) for w in raw_input().split()]
    Q.append((l,r))

for i in xrange(NQ):
    l, r = Q[i]
    s1 = S[l-1:r]
    m = r - l + 1

    n_similars = 1
    for k in xrange(0, N-m+1):
        if k != l-1:
            s2 = S[k:k+m]

            if s1 == s2:
                n_similars += 1
            elif check1(s1, s2):
                n_similars += 1

    print n_similars


