

class Node:
    def __init__(self, key, heap_id):
        self.key = key
        self.n = self.size = 1
        self.heap_id = heap_id
        self.parent = self.left = self.right = None

rnd = 1
pool = []

def new_node(key):
    if pool:
        node = pool.pop()
        node.key = key
        node.heap_id = rand()
        node.parent = node.left = node.right = None
        node.n = node.size = 1
    else:
        node = Node(key, rand())

    return node


def release_node(node):
    pool.append(node)


def rand():
    global rnd
    rnd += 1
    return (rnd * 2654435761) % (2**32)


class IndexTreap:
    def __init__(self):
        self.root = None

    def add(self, key):
        node, parent = IndexTreap._find(key, self.root)
        if node:
            node.n += 1
            node.size += 1
            IndexTreap._bal(node.parent)
        else:
            node = new_node(key)
            if parent:
                node.parent = parent
                if node.key > parent.key:
                    parent.right = node
                else:
                    parent.left = node
            else:
                self.root = node

            self._prioritize(node)

        return node

    def _remove(self, node):
        node.n -= 1
        node.size -= 1
        if node.n > 0:
            IndexTreap._bal(node.parent)
            return

        if not node.parent and not (node.left and node.right):
            self.root = node.left or node.right
            if self.root:
                self.root.parent = None
        else:
            while node.left and node.right:
                if node.left.heap_id <= node.right.heap_id:
                    self._up(node.right)
                else:
                    self._up(node.left)

            child = node.left or node.right
            parent = node.parent

            if parent.right == node:
                parent.right = child
            else:
                parent.left = child

            if child:
                child.parent = parent

            while parent:
                parent.size = parent.n + (parent.left.size if parent.left else 0) + (parent.right.size if parent.right else 0)
                parent = parent.parent

        release_node(node)

    def r_rank(self, node):
        r = node.right.size if node.right else 0
        if node:
            parent = node.parent
            while parent:
                if parent.left == node:
                    r += (parent.right.size if parent.right else 0) + parent.n

                node = parent
                parent = parent.parent

        return r

    def l_rank(self, node):
        r = node.left.size if node.left else 0
        if node:
            parent = node.parent
            while parent:
                if parent.right == node:
                    r += (parent.left.size if parent.left else 0) + parent.n

                node = parent
                parent = node.parent

        return r

    def _prioritize(self, node):
        while node.parent and node.parent.heap_id < node.heap_id:
            self._up(node)

        while node:
            node.size = node.n + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
            node = node.parent

    @staticmethod
    def _bal(node):
        while node:
            size = node.size
            node.size = node.n + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
            if size == node.size:
                break

            node = node.parent

    def _up(self, node):
        parent = node.parent

        if parent.right == node:
            parent.right = node.left

            if node.left:
                node.left.parent = parent

            node.left = parent
        else:
            parent.left = node.right

            if node.right:
                node.right.parent = parent

            node.right = parent

        node.parent = None

        grandparent = parent.parent
        if grandparent:
            if grandparent.right == parent:
                grandparent.right = node
            else:
                grandparent.left = node

            node.parent = grandparent
        else:
            self.root = node
            node.parent = None

        parent.parent = node

        parent.size = parent.n + (parent.left.size if parent.left else 0) + (parent.right.size if parent.right else 0)
        node.size = node.n + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)


    @staticmethod
    def _find(key, node):
        parent = node.parent if node else None
        while node and key != node.key:
            parent = node
            node = node.right if key > node.key else node.left

        return node, parent

    @staticmethod
    def _set_child(node, child, new_child):
        if node.right == child:
            node.right = new_child
        else:
            node.left = new_child

        if new_child:
            new_child.parent = node

        child.parent = None


def inversionCount(n, m, a):
    global pool
    pool = [Node(0,0) for _ in range(m+1)]
    t = IndexTreap()
    ri = 0
    for i in range(m-1):
        ri += t.r_rank(t.add(a[i]))

    ri += t.r_rank(t.add(a[m-1]))
    tot_ranks = ri

    for i in range(m, n):
        ri += t.r_rank(t.add(a[i]))

        node, _ = IndexTreap._find(a[i-m], t.root)
        ri -= t.l_rank(node)
        t._remove(node)

        tot_ranks += ri

    return tot_ranks



t = IndexTreap()

if 0:
    n, m = 4, 3
    a = [1, 4, 3, 2]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()

if 0:
    n, m = 5, 2
    a = [100, 5, 100, 5, 5]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()

if 0:
    n, m = 10, 5
    a = [15, 51, 44, 44, 76, 50, 29, 88, 48, 50]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()

if 1:
    n = 5 * 10**5
    m = n - 100

    a = list(reversed(range(n)))
    res = inversionCount(n, m, a)
    print(res)
