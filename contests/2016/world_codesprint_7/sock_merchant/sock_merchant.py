# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
C = [int(c) for c in raw_input().split()]
d = {}
for c in C:
    d[c] = d.get(c, 0) + 1
            
npairs = 0
for (c, n) in d.iteritems():
    npairs += n/2
                        
print npairs
