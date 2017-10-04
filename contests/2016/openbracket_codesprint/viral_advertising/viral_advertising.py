
n = int(input())

nodes = 2
tot = 2

for i in range(2, n+1):
    nodes *= 3
    liked = nodes // 2
    tot += liked
    nodes = liked
    
print(tot)

