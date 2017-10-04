
for _ in range(int(input())):
    n = int(input())
    a = [int(w) for w in input().split()]
    assert len(a) == n
    if n <= 3:
        print(sum(a))
    else:
        a.reverse()
        f0, f1, f2 = 0, a[0], a[0]+a[1]
        s = sum(a[:2])
        for i in range(3, n+1):
            s += a[i-1]
            f0, f1, f2 = f1, f2, s - min(f0, f1, f2)
        print(f2)

