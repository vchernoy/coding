
for _ in range(int(input())):
    n = int(input())
    a = [int(w) for w in input().split()]
    assert len(a) == n
    r = 0
    for i in range(n):
        k = (i+1) * (n-i)
        if k % 2 == 1:
            r = r ^ a[i]
            
    print(r)

