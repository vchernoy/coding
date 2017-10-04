

def solve(n, p, a):
    tree = {}
    for i in range(n-1):
        v = i + 1
        u = p[i] - 1
        tree[v] = u
        # tree[v] = u

    print(tree)

n = int(input().strip())
p = [int(w) for w in input().strip().split(' ')]

a = [int(w) for w in input().strip().split(' ')]

assert n % 2 == 0
assert 1 <= n <= 2 * 10**5
assert len(p) == n-1
assert max(p) <= n
assert min(p) >= 1

assert len(a) == n
assert set(a) == set(range(1,n//2+1))

res = solve(n, p, a)

print(res)