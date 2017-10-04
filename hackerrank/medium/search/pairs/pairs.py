
n, k = [int(w) for w in raw_input().split()]
a = [int(w) for w in raw_input().split()]

s = set(a)

count = 0
for x in a:
    y = x + k
    if y in s:
        count += 1

print count

