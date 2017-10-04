#!/Users/slava/work/fb_hacker_cup/venv/bin/python

t = 100
n = 100
m = 5000
k = 5000


print(t)
for _ in range(t):
    print(n, m, k)
    for i in range(m):
        print(i // n + 1, i % n + 1, 1000)

    for s in range(k):
        print((s + 23) % n + 1, (s + 1117) % n + 1)
