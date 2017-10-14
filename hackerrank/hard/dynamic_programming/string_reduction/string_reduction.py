
C = {'ab':'c', 'ba':'c', 'ac':'b', 'ca':'b', 'cb':'a', 'bc':'a'}

N = {
    'abc':{},
    'acb':{'c':'b', 'b':'c'},
    'bac':{'a':'b', 'b':'a'},
    'bca':{'b':'a', 'c':'b', 'a':'c'},
    'cab':{'c':'a', 'a':'b', 'b':'c'},
    'cba':{'c':'a', 'a':'c'},
    'ab':{},
    'ac':{'c':'b'},
    'ba':{'b':'a', 'a':'b'},
    'bc':{'b':'a', 'c':'b'},
    'ca':{'c':'a', 'a':'b'},
    'cb':{'c':'a'},
    'a':{},
    'b':{'b':'a'},
    'c':{'c':'a'},
    '': {}
    }

def norma(s):
    global N

    X = [(s.find(c), c) for c in 'abc']
    X = [x if x[0] >= 0 else (len(s), x[1]) for x in X]
    X.sort()
    y = ''.join([x[1] for x in X if x[0] < len(s)])

    N0 = N[y]
    if len(N0) == 0:
        pass
    elif len(N0) == 1:
        c = N0.keys()[0]
        s = s.replace(c, N0[c])
    else:
        s = ''.join([N0.get(c, c) for c in s])

    return s

DF = {'':0, 'a':1}
def F(s):
    global DF, C

    s = norma(s)
    n = DF.get(s, -1)
    if n == -1:
        n = len(s)
        for i in xrange(len(s)-1):
            if s[i] != s[i+1]:
                break

        if s[i] != s[i+1]:
            s1 = s[:i] + C[s[i:i+2]] + s[i+2:]
            n = min(n, F(s1))

            i += 1

            if (n > 1) and (i < len(s) - 2) and (s[i] != s[i+1]):
                s1 = s[:i] + C[s[i:i+2]] + s[i+2:]
                n = min(n, F(s1))

        DF[s] = n

    return n

for i in xrange(int(raw_input())):
    s = raw_input()
    print F(s)

