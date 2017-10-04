
class Node:
    def __init__(self, id):
        self.id = id
        self.children = {}
        self.count = 1
        
    def add_child(self, c):
        assert c.id not in self.children
        self.children[c.id] = c
        self.count += c.count
        
def to_tree(id, graph):
    root = Node(id)
    for cid in graph[id]:
        graph[cid].remove(id)
        root.add_child(to_tree(cid, graph))
    return root

def Func(root):
    assert root.count > 0
    if root.count <= 2:
        return 0
    
    r = 0
    for c in root.children.values():
        if c.count % 2 == 0:
            r += Func(c) + 1
        else:
            r += Func(c)
            
    return r
            
n, m = [int(w) for w in input().split()]
assert m == n-1
graph = {}
for i in range(m):
    u, v = [int(w) for w in input().split()]
    u -= 1
    v -= 1
    graph.setdefault(u,set()).add(v)
    graph.setdefault(v,set()).add(u)
    
root = to_tree(0, graph)

res = Func(root)
print(res)

