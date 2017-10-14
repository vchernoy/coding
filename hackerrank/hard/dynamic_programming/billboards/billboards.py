
import heapq

n, k = [int(w) for w in raw_input().split()]

p = [0] * (n+1)
for i in xrange(n):
    p[i] = int(raw_input())

sp = [0] * (n+1)
for i in xrange(n):
    sp[i+1] = sp[i] + p[i]

que = []

heapq.heappush(que, (-sp[n], -1))

res = 0
for i in xrange(0, n+1):
    while que[0][1] < i - k - 1:
        heapq.heappop(que)

    mx = -que[0][0];
    res = max(mx - sp[n] + sp[i], res)
    heapq.heappush(que, (-(mx - p[i]), i));

print res

