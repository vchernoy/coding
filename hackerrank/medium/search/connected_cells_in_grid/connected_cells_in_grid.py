
def size(y, x):
    global A
    
    A[y][x] = 0
    size = 1
    que = [(y, x)]
    while que:
        y, x = que.pop()
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            x1 = x + dx
            y1 = y + dy
            if A[y1][x1]:
                que.append((y1, x1))
                A[y1][x1] = 0
                size += 1
 
    return size

n = int(input())
m = int(input())

A = [[0] * (m + 2)]
for _ in range(n):
    a = [0] + [int(w) for w in input().split()] + [0]
    A.append(a)

A.append([0] * (m + 2))

n += 2
m += 2
max_size = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if A[i][j]:
            sz = size(i, j)
            max_size = max(sz, max_size)
            
print(max_size)

