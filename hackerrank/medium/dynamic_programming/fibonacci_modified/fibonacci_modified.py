
t1, t2, n = [int(w) for w in input().split()]

for _ in range(2, n):
    t1, t2 = t2, t1 + t2**2
    
print(t2)

