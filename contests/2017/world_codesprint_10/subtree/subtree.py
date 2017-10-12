# Enter your code here. Read input from STDIN. Print output to STDOUTimport sys

import sys

def F(tree, r, w, weights, visited):
    visited.add(r)
    for x in tree.get(r,set()):
        if x not in visited:
            F(tree, x, w, weights, visited)

    #print(weights)

    #print(w, r)
    max_s = w[r]
    for x in tree.get(r,set()):
        if x not in visited:
            max_s = max(max_s, weights[x])

    max_s = max(max_s, w[r])

    max_s1 = []
    for x in tree.get(r,set()):
        if x not in visited:
            x_s1 = weights[(x, 1)]
            if x_s1 >= 0:
                max_s1.append(x_s1)

    max_s1 = w[r] + sum(max_s1)

    weights[(r,1)] = max_s1
    weights[r] = max(max_s, max_s1)

    visited.remove(r)


def solve(n, w, u, v):
    assert len(w) == n
    assert len(u) == n-1
    assert len(v) == n-1

    res = []

    tree = {}
    for i in range(n-1):
        x, y = u[i], v[i]
        tree.setdefault(x, set()).add(y)
        tree.setdefault(y, set()).add(x)

    print(w)
    print(tree)

    for i in range(n-1):
        x, y = u[i], v[i]

        tree.setdefault(x, set()).remove(y)
        tree.setdefault(y, set()).remove(x)

        weights = {}
        F(tree, x, w, weights, set())
        F(tree, y, w, weights, set())
        rxy = weights[x] * weights[y]
        res.append(rxy)
        print(x, y, ':', weights[x], weights[y], rxy)
        print(weights)

        tree.setdefault(x, set()).add(y)
        tree.setdefault(y, set()).add(x)

    return max(res)


if 1:
    w = [1,1,1]
    u=[0,1]
    v=[1,2]
    n = len(w)

    print(w)
    res0 = solve(n, w, u, v)
    res1 = solve(n, [-x for x in w], u, v)
    print(res0, res1, max(res0, res1))

    sys.exit(0)

n = int(input().strip())
# The respective weights of each node:
w = list(map(int, input().strip().split(' ')))
u = [0] * (n-1)
v = [0] * (n-1)
for i in range(n-1):
    # Node IDs 'u' and 'v' are connected by an edge:
    ui, vi = [int(tok) for tok in input().strip().split(' ')]
    u[i] = ui-1
    v[i] = vi-1

print(w)
res0 = solve(n, w, u, v)
res1 = solve(n, [-x for x in w], u, v)
print(res0, res1, max(res0, res1))



