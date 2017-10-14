
n = int(input())
t = [int(w) for w in input().split()]
ivs = []
n_ready = 0
for i in range(n):
    ti = t[i]
    if ti == 0:
        n_ready += 1
    elif ti < n:
        if ti <= i:
            ivs.append((0, i - ti))
            if i < n-1:
                ivs.append((i+1, n-1))
        else:
            ivs.append((i+1, n - ti + i))

p = []
for iv in ivs:
    p.append((iv[0], True))
    p.append((iv[1]+1, False))

p.sort()
p.append((-1, True))
overlaps = 0
max_overlaps = 0
prev_x = -1
best_x = 0
for x, beg in p:
    if x != prev_x:
        if max_overlaps < overlaps:
            max_overlaps = overlaps
            best_x = prev_x

        prev_x = x

    if beg:
        overlaps += 1
    else:
        overlaps -= 1

print(best_x + 1)

