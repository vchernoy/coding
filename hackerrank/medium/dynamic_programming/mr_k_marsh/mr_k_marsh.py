
m, n = [int(w) for w in input().split()]

A = []
for _ in range(m):
    A.append([(1 if w == 'x' else 0) for w in input()])
    
L = [[0] * n for _ in range(m)]
R = [[0] * n for _ in range(m)]
U = [[0] * n for _ in range(m)]
D = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if A[i][j] == 0:
            L[i][j] = 1
            if j > 0:
                L[i][j] = L[i][j-1] + 1

            U[i][j] = 1
            if i > 0:
                U[i][j] = U[i-1][j] + 1

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        if A[i][j] == 0:
            R[i][j] = 1
            if j < n-1:
                R[i][j] = R[i][j+1] + 1

            D[i][j] = 1
            if i < m-1:
                D[i][j] = D[i+1][j] + 1

best_p = 0
for y in range(m):
    for x in range(n):
        y1 = y+D[y][x] - 1
        x1 = x+R[y][x]
        p = 2*(x1 - x) + 2*(y1 - y)
        if p > best_p:
            for y1 in range(y+1, y+D[y][x]):
                for x1 in range(x+1, x+R[y][x]):
                    if (R[y][x] > x1 - x) and (D[y][x] > y1 - y) and (L[y1][x1] > x1 - x) and (U[y1][x1] > y1 - y):
                        p = 2*(x1 - x) + 2*(y1 - y)
                        best_p = max(best_p, p)
                    
print(best_p if best_p else "impossible ")

