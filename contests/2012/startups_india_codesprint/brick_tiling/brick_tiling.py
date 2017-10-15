
def put(i, j, shape):
    global A, n, m

    for (x, y) in shape:
        if A[i + x][j + y] != 0:
            return False

    for (x, y) in shape:
        A[i + x][j + y] = 1

    return True

def clear(i, j, shape):
    global A, n, m

    for (x, y) in shape:
        A[i + x][j + y] = 0

def code(i):
    global A, n, m
    
    while (i <= n) and (0 not in A[i]):
        i += 1

    s = 255
    for i1 in xrange(i, n+1):
        ch = 0
        if 1 in A[i1][1:-1]:
            for j in xrange(1, m+1):
                ch = ch * 2 + A[i1][j]

        s = s * 256 + ch

    return s 

def compute(i, j):
    global Shapes, A, n, m, D, Mod

    while (i <= n) and (0 not in A[i][j:]):
        i += 1
        j = 1

    if i <= n:
        c = code(i)
        if c in D:
            return D[c]

        j = A[i].index(0, j)
        res = 0
        for shape in Shapes:
            if put(i, j, shape):
                res = (res + compute(i, j+1)) % Mod
                clear(i, j, shape)

        D[c] = res
    else:
        res = 1

    return res


Mod = 1000000007

Shapes = []

Shapes.append([(0,0), (1,0), (2,0), (2,1)])
Shapes.append([(0,0), (0,1), (0,2), (1,2)])

Shapes.append([(0,0), (1,0), (0,1), (0,2)])
Shapes.append([(0,0), (0,1), (1,0), (2,0)])

Shapes.append([(0,0), (1,0), (2,0), (2,-1)])
Shapes.append([(0,0), (0,1), (1,1), (2,1)])
Shapes.append([(0,0), (1,0), (1,-1), (1,-2)])
Shapes.append([(0,0), (1,0), (1,1), (1,2)])

for t in xrange(int(raw_input())):
    n, m = [int(w) for w in raw_input().split()]
    A = [[1]*(m+2) for i in xrange(n+2)]

    for i in xrange(n):
        l = raw_input()
        assert(len(l) == m)
        for j in xrange(m):
            A[i+1][j+1] = 1 if l[j] == '#' else 0

    D = {}
    print compute(1, 1)

