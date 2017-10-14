
import random, time

def path(graph):
    n = len(graph)
    best_p = []
    while time.time() < end:
        cur = random.randint(0, n-1)
        p = [cur]
        visited = set(p)
        while True:
            options = graph[cur].difference(visited)
            if not options:
                break
            if len(options) == 1:
                cur = options.pop()
            else:
                cur = random.choice(list(options)) # options.pop()
            visited.add(cur)
            p.append(cur)

        if len(p) >= 2:
            cur = p[-2]
            options = graph[cur].difference(visited)
            if options:
                bad = p[-1]
                visited.remove(bad)
                p.pop()
                cur = options.pop()
                visited.add(cur)
                p.append(cur)
                while True:
                    options = graph[cur].difference(visited)
                    if not options:
                        break
                    if len(options) == 1:
                        cur = options.pop()
                    else:
                        cur = random.choice(list(options)) # options.pop()
                    visited.add(cur)
                    p.append(cur)

        if len(p) >= 2:
            cur = p[-2]
            options = graph[cur].difference(visited)
            if options:
                bad = p[-1]
                visited.remove(bad)
                p.pop()
                cur = options.pop()
                visited.add(cur)
                p.append(cur)
                while True:
                    options = graph[cur].difference(visited)
                    if not options:
                        break
                    if len(options) == 1:
                        cur = options.pop()
                    else:
                        cur = random.choice(list(options)) # options.pop()
                    visited.add(cur)
                    p.append(cur)

        if len(p) > len(best_p):
            best_p = p

        options = graph[p[0]].difference(visited)
        if options:
            p2 = []
            cur = options.pop()
            visited.add(cur)
            p2 = [cur]
            while True:
                options = graph[cur].difference(visited)
                if not options:
                    break
                if len(options) == 1:
                    cur = options.pop()
                else:
                    cur = random.choice(list(options)) # options.pop()
                visited.add(cur)
                p2.append(cur)
                
            if len(p2) >= 2:
                cur = p2[-2]
                options = graph[cur].difference(visited)
                if options:
                    bad = p2[-1]
                    visited.remove(bad)
                    p2.pop()
                    cur = options.pop()
                    visited.add(cur)
                    p2.append(cur)
                    while True:
                        options = graph[cur].difference(visited)
                        if not options:
                            break
                        if len(options) == 1:
                            cur = options.pop()
                        else:
                            cur = random.choice(list(options)) # options.pop()
                        visited.add(cur)
                        p2.append(cur)

            if len(p2) >= 2:
                cur = p2[-2]
                options = graph[cur].difference(visited)
                if options:
                    bad = p2[-1]
                    visited.remove(bad)
                    p2.pop()
                    cur = options.pop()
                    visited.add(cur)
                    p2.append(cur)
                    while True:
                        options = graph[cur].difference(visited)
                        if not options:
                            break
                        if len(options) == 1:
                            cur = options.pop()
                        else:
                            cur = random.choice(list(options)) # options.pop()
                        visited.add(cur)
                        p2.append(cur)

            p2.reverse()
            p = p2 + p

            if len(p) > len(best_p):
                best_p = p
                        
    return best_p
        
start = time.time()
end = start + 3.95
random.seed()

n, m = [int(w) for w in input().split()]
graph = [set() for _ in range(n)]
for _ in range(m):
    x, y = [int(w) for w in input().split()]
    x -= 1
    y -= 1
    graph[x].add(y)
    graph[y].add(x)
    
p = path(graph)
print(len(p))
print(' '.join([str(x+1) for x in p]))

