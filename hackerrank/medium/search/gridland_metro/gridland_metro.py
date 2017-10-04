
n, m, k = [int(w) for w in raw_input().split()]

tracks = []

for i in xrange(k):
    r, c1, c2 = [int(w) for w in raw_input().split()]
    tracks.append((r, c1, c2))
    
d = {}
for t in tracks:
    r, c1, c2 = t
    d.setdefault(r, []).append((c1, c2))
    
res = n * m
for r in d.iterkeys():
    line = d[r]
    beg = {}
    end = {}
    points = set([0, (m+1)])
    for t in line:
        c1, c2 = t
        c2 += 1
        points.add(c1)
        points.add(c2)
        beg[c1] = beg.get(c1, 0) + 1
        end[c2] = end.get(c2, 0) + 1

    points = [p for p in points]
    points.sort()
    
    val = 0
    prev_point = 0
    n_tracks = 0
    for p in points:
        n_beg = beg.get(p, 0)
        n_end = end.get(p, 0)
        if n_tracks > 0:
            val += p - prev_point
            
        n_tracks += n_beg - n_end
        prev_point = p
        
    res -= val
        
print res

