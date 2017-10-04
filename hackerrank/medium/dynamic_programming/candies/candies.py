
def count(r):
    n = len(r)
    f = [None] * n
    
    if r[0] <= r[1]:
        f[0] = 1
    if r[-1] <= r[-2]:
        f[-1] = 1
    for i in range(1, n-1):
        if (r[i] <= r[i-1]) and (r[i] <= r[i+1]):
            f[i] = 1

    for i in range(1,n):
        if (r[i] > r[i-1]) and f[i-1]:
            f[i] = f[i-1] + 1
            

    for i in range(n-2,-1,-1):
        if (r[i] > r[i+1]) and f[i+1]:
            if f[i]:
                f[i] = max(f[i], f[i+1] + 1)
            else:
                f[i] = f[i+1] + 1

    return sum(f)

n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))

print(count(r))

