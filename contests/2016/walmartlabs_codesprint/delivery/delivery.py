
def dist(u, v):
    global Levels
    
    if Levels[u] < Levels[v]:        
        u, v = v, u

    dl = Levels[u] - Levels[v]
    for i in range(dl):
        u //= 2

    l = 0
    while v != u:
        l += 1
        v //= 2
        u //= 2

    return 2*l + dl

N, M, Q = [int(w) for w in input().split()]
foods = []
for i in range(M):
    arr = [int(w) for w in input().split()]
    restaurants = set(arr[1:])
    foods.append(restaurants)
    
requests = []
for i in range(Q):
    food, person = [int(w) for w in input().split()]
    requests.append((food, person))

INF = 10**7
pos = 1
tot_path = 0

Levels = {}
n = 1
for l in range(17):
    for i in range(2**l):
        Levels[n] = l
        n += 1

for food, person in requests:
    if pos == person:
        best_path = INF
        for r in foods[food-1]:
            path = dist(pos, r)
            best_path = min(path, best_path)
        best_path *= 2
    elif (pos in foods[food-1]) or (person in foods[food-1]):
        best_path = dist(pos, person)
    else:
        best_path = INF
        for r in foods[food-1]:
            path = dist(pos, r) + dist(r, person)
            best_path = min(path, best_path)

    tot_path += best_path
    pos = person
    
print(tot_path)

