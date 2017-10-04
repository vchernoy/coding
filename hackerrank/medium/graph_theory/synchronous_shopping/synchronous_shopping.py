
def dijkstra(src):
    global N, Z

    dist = [-1] * N
    dist[src] = 0

    que = list(range(N))
    while que:
        j = 0
        dist_u = dist[que[0]]
        for i in range(1, len(que)):
            dist_v = dist[que[i]]
            if (dist_u < 0) or (dist_v >= 0 and dist_v <= dist_u):
                dist_u = dist_v
                j = i

        u = que[j]
        que[j] = que[-1]
        que.pop()

        assert dist_u >= 0

        for v in range(N):
            if Z[u][v] > 0:
                alt = dist_u + Z[u][v]
                if (dist[v] < 0) or (alt < dist[v]):
                    dist[v] = alt

    return dist


visited = set()

def f(src, dest, types):
    global Z, A, D, N

    types = types & (~A[dest])
    if src == dest:
        if types == 0:
            return 0

    if types == 0:
        return D[src][dest]

    k = (src, dest, types)
    if k in visited:
        return -1

    visited.add(k)

    dist = -1
    for v in range(N):
        if Z[v][dest] > 0:
            df = f(src, v, types)
            if df >= 0:
                dist_v = df + Z[v][dest]
                if (dist < 0) or (dist_v < dist):
                    dist = dist_v

    visited.remove(k)

    return dist


N, M, K = [int(w) for w in input().split()]
assert N >= 2
assert M >= 1
assert K >= 1

T = [0] * N
A = [0] * N

for i in range(N):
    arr = [int(w) for w in input().split()]
    T[i] = arr[0]
    a = [f-1 for f in arr[1:]]
    assert len(a) == T[i]
    assert len(set(a)) == T[i]
    assert max(a) <= K-1
    assert min(a) >= 0

    A[i] = sum([2**f for f in a])

Z = [[-1] * N for _ in range(N)]

for j in range(M):
    x, y, z = [int(w) for w in input().split()]
    x -= 1
    y -= 1

    assert z >= 1
    assert Z[x][y] < 0
    assert Z[y][x] < 0
    assert x != y

    Z[x][y] = z
    Z[y][x] = z

D = [[] for _ in range(N)]

for src in range(N):
    D[src] = dijkstra(src)

#print(Z)
#print(D)

shortest_time = 10**(3+3+4+1)
for types1 in range(2**K):
    types2 = 2**K - 1 - types1

    time = max(f(0, N-1, types1 & (~A[0])), f(0, N-1, types2 & (~A[0])))
    shortest_time = min(shortest_time, time)

print(shortest_time)