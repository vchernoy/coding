
import os
import unittest
import random


class Node:
    def __init__(self, key, heap_id):
        self.key = key
        self.n = 1
        self.size = 1
        self.heap_id = heap_id
        self.parent = None
        self.child = {False: None, True: None}

    def __repr__(self):
        return str((self.key, self.n, self.size, self.heap_id))


class Treap:
    """
    Treap
    >>> treap = Treap()
    >>> len(treap)
    0
    >>> treap.add('a')
    >>> 'a' in treap
    True
    >>> len(treap)
    1
    >>> treap.lrank('a')
    0
    >>> treap.add('b')
    >>> 'b' in treap
    True
    >>> len(treap)
    2
    >>> treap.lrank('a')
    0
    >>> treap.lrank('b')
    1
    >>> treap.add('a')
    >>> 'a' in treap
    True
    >>> len(treap)
    3
    >>> treap.lrank('a')
    0
    >>> treap.lrank('b')
    2
    >>> treap.remove('b')
    >>> 'b' in treap
    False
    >>> len(treap)
    2
    >>> treap.remove('a')
    >>> 'a' in treap
    True
    >>> treap.lrank('a')
    0
    >>> len(treap)
    1
    >>> treap.remove('a')
    >>> 'a' in treap
    False
    >>> len(treap)
    0
    """
    def __init__(self, rand=random.Random(0), max_heap_id=2**31):
        self.rand = rand
        self.max_heap_id = max_heap_id
        self.root = None

    def __len__(self):
        return Treap._size(self.root)

    @staticmethod
    def _size(node):
        return node.size if node else 0

    @staticmethod
    def _update_size(node):
        if node:
            node.size = node.n + Treap._size(node.child[False]) + Treap._size(node.child[True])

    @staticmethod
    def _set_child(node, child, new_child):
        assert node
        is_right = node.child[True] == child
        assert node.child[is_right] == child
        if child != new_child:
            node.child[is_right] = new_child
            if new_child:
                new_child.parent = node

            if child:
                child.parent = None

    def add(self, key):
        """Set a key, value pair in the tree."""
        node, parent = Treap._find_node(key, self.root)
        if node:
            node.n += 1
        else:
            heap_id = self.rand.randrange(self.max_heap_id)
            node = Node(key, heap_id)
            if parent:
                node.parent = parent
                parent.child[node.key > parent.key] = node
            else:
                self.root = node

        self._prioritize(node)

    @staticmethod
    def _find_node(key, node, parent=None):
        while node and key != node.key:
            node, parent = node.child[key > node.key], node

        return node, parent

    def _pivot_up(self, node):
        """
        parent.left == node:
        Given the following binary search tree:
               5
              / \
             3   C
            / \
           A   B
        Imagine we need to pivot 3 and 5 (to maintain the heap
        property). The resulting tree will look like:
               3
              / \
             A   5
                / \
               B   C
        """
        parent = node.parent
        if not parent:
            return

        is_right = parent.child[True] == node
        Treap._set_child(parent, node, node.child[not is_right])

        node.child[not is_right] = parent

        grandparent = parent.parent
        if grandparent:
            Treap._set_child(grandparent, parent, node)
        else:
            self.root = node
            node.parent = None

        parent.parent = node
        Treap._update_size(parent)
        Treap._update_size(node)

    def _prioritize(self, node):
        while node.parent and node.parent.heap_id < node.heap_id:
            self._pivot_up(node)

        while node:
            Treap._update_size(node)
            node = node.parent

    def __contains__(self, key):
        """Return True iff key is found in tree, else False."""
        node, _ = Treap._find_node(key, self.root)
        return node is not None

    def remove(self, key):
        """Delete a key, value pair identified by key from the tree."""
        node, parent = Treap._find_node(key, self.root)
        if not node:
            raise KeyError(key)

        node.n -= 1
        if node.n > 0:
            self._prioritize(node)
            return

        if not parent and not (node.child[False] and node.child[True]):
            self.root = node.child[False] or node.child[True]
            if self.root:
                self.root.parent = None
        else:
            while node.child[False] and node.child[True]:
                # Pivot a child node up while the node to be deleted has
                # both left and right children.
                is_right = node.child[False].heap_id <= node.child[True].heap_id
                self._pivot_up(node.child[is_right])

            child = node.child[False] or node.child[True]
            parent = node.parent
            Treap._set_child(parent, node, child)
            self._prioritize(parent)

        node.parent = None
        node.child[False] = None
        node.child[True] = None

    def min(self):
        """Return the minimum key."""
        if not self.root:
            return None

        node, parent = Treap._traverse(self.root, 'left')
        return node.key

    def max(self):
        """Return the maximum key."""
        if not self.root:
            return None

        node, parent = Treap._traverse(self.root, 'right')
        return node.key

    def clear(self):
        """Clear all the (key, value) pairs from the tree."""
        self.root = None

    @staticmethod
    def _traverse(node, attr, parent=None):
        while getattr(node, attr):
            node, parent = getattr(node, attr), node

        return node, parent

    def lrank(self, key):
        return self.rank(key, False)


    def rrank(self, key):
        return self.rank(key, True)

    def rank(self, key, is_right):
        node, _ = Treap._find_node(key, self.root)
        if not node:
            raise KeyError(key)

        r = Treap._size(node.child[is_right])
        while node:
            parent = node.parent
            if parent and parent.child[not is_right] == node:
                r += Treap._size(parent.child[is_right]) + parent.n

            node = parent

        return r

    def check(self):
        """Check treap invariants."""
        nodes = [(self.root, -self.max_heap_id, self.max_heap_id)]
        while nodes:
            node, min_bound, max_bound = nodes.pop()
            if node:
                assert min_bound < node.key < max_bound
                if node.child[False]:
                    assert node.key > node.child[False].key

                if node.child[True]:
                    assert node.key < node.child[True].key

                if node.parent:
                    parent = node.parent
                    assert node.heap_id < parent.heap_id
                    assert parent.child[False] == node or parent.child[True] == node

                nodes.append((node.child[False], min_bound, node.key))
                nodes.append((node.child[True], node.key, max_bound))

    def __repr__(self):
        """Return a string representation of treap."""
        lines = []
        nodes = [(self.root, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node) if node else 'None'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.child[True], indent + 1))
                nodes.append((node.child[False], indent + 1))

        return os.linesep.join(lines)

#
# class TestTreap(unittest.TestCase):
#     def setUp(self):
#         self.treap = Treap()
#
#     def test_tree(self):
#         treap = self.treap
#         treap.add(1)
#         treap.add(2)
#         treap.add(0)
#         self.assertEqual(repr(treap), repr(treap))
#
#         self.assertIn(1, treap)
#         treap.add(1)
#         self.assertIn(1, treap)
#         self.assertRaises(KeyError, treap.remove, 3)
#
#         self.assertIn(1, treap)
#         self.assertNotIn(3, treap)
#
#         treap.remove(1)
#         treap.remove(2)
#         treap.remove(1)
#         treap.remove(0)
#         treap.remove(1)
#         self.assertRaises(KeyError, treap.remove, 1)
#
#         treap.add(5)
#         treap.add(3)
#         treap.add(1)
#         treap.add(2)
#         treap.add(4)
#         treap.add(9)
#         treap.add(7)
#         treap.add(6)
#         treap.add(8)
#
#         self.assertEqual(treap.min(), 1)
#         self.assertEqual(treap.max(), 9)
#         treap.check()
#
#         treap.remove(3)
#         treap.remove(9)
#         treap.remove(5)
#         treap.remove(2)
#         treap.clear()
#         self.assertEqual(treap.min(), None)
#         self.assertEqual(treap.max(), None)
#
#     def test_stress(self):
#         try:
#             from progressbar import ProgressBar
#         except ImportError:
#             ProgressBar = lambda: iter
#
#         rand = random.Random(0)
#         treap = self.treap
#         treap.clear()
#         keys = range(10000)
#
#         rand.shuffle(keys)
#         progress = ProgressBar()
#         for key in progress(keys):
#             treap.add(key)
#             treap.check()
#
#         rand.shuffle(keys)
#         progress = ProgressBar()
#         for key in progress(keys):
#             assert key in treap
#
#         rand.shuffle(keys)
#         progress = ProgressBar()
#         for key in progress(keys):
#             treap.remove(key)
#             assert key not in treap
#             treap.check()


def inversionCount(n, m, a):
    t = Treap()
    tot_ranks = 0
    ri = 0
    for i in range(n):
        if i < n:
            t.add(a[i])
            rrai = t.rrank(a[i])
            ri += rrai

        j = i - m
        if 0 <= j < n:
            lraj = t.lrank(a[j])
            t.remove(a[j])
            ri -= lraj

        if i >= m-1:
            tot_ranks += ri
            # print(ri,)

    return tot_ranks

# if __name__ == '__main__':
#     unittest.main()


t = Treap()

if 1:
    n, m = 4, 3
    a = [1, 4, 3, 2]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()


if 1:
    n, m = 5, 2
    a = [100, 5, 100, 5, 5]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()

if 1:
    n, m = 10, 5
    a = [15, 51, 44, 44, 76, 50, 29, 88, 48, 50]
    res = inversionCount(n, m, a)
    print()
    print(res)
    print()

