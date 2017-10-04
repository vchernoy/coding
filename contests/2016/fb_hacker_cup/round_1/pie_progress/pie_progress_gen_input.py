#!/Users/slava/work/fb_hacker_cup/venv/bin/python

t = 100
n = 300
m = 300
print(t)
for _ in range(t):
    print(n, m)
    for i in range(n):
        ci = []
        for j in range(m):
            ci.append(1000000 - i - j*j)

        print(' '.join([str(cij) for cij in ci]))

