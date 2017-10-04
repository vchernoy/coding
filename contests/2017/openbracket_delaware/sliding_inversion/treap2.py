
import os
import unittest
import random


class Node:
    def __init__(
            self, key, value, heap_id,
            parent=None, left=None, right=None
    ):
        self.key = key
        self.value = value
        self.heap_id = heap_id
        self.parent = parent
        self.child = {False: left, True: right}

    def __repr__(self):
        return str((self.key, self.value, self.heap_id))


class Treap:
    """
    Treap
    >>> treap = Treap()
    >>> treap['a'] = 1
    >>> treap['a']
    1
    >>> treap['b'] = 2
    >>> 'b' in treap
    True
    >>> del treap['b']
    >>> 'b' in treap
    False
    """
    def __init__(self, rand=random.Random(0), max_heap_id=2**31):
        self.rand = rand
        self.max_heap_id = max_heap_id
        self.root = None

    def __setitem__(self, key, value):
        """Set a key, value pair in the tree."""
        node, parent = Treap._find_node(key, self.root)
        if not node:
            heap_id = self.rand.randrange(self.max_heap_id)
            node = Node(key, value, heap_id)
            if not parent:
                self.root = node
            else:
                parent.child[node.key > parent.key] = node

            node.parent = parent
            self._prioritize(node)
        else:
            node.value = value

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
        node.child[not is_right], parent.child[is_right] = parent, node.child[not is_right]
        if parent.child[is_right]:
            parent.child[is_right].parent = parent

        grandparent = parent.parent
        node.parent, parent.parent = grandparent, node
        if grandparent:
            grandparent.child[grandparent.child[True] == parent] = node
        else:
            self.root = node

    def _prioritize(self, node):
        while node.parent and node.parent.heap_id < node.heap_id:
            self._pivot_up(node)

    def __contains__(self, key):
        """Return True iff key is found in tree, else False."""
        node, _ = Treap._find_node(key, self.root)
        return node is not None

    def __getitem__(self, key):
        """Return the value corresponding to key in the tree."""
        node, _ = Treap._find_node(key, self.root)
        if not node:
            raise KeyError(key)

        return node.value

    def __delitem__(self, key):
        """Delete a key, value pair identified by key from the tree."""
        node, parent = Treap._find_node(key, self.root)
        if not node:
            raise KeyError(key)

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
            node.parent.child[node.parent.child[True] == node] = child

            if child:
                child.parent = node.parent

        node.parent = None
        node.child[False] = None
        node.child[True] = None

    def min(self):
        """Return the (key, value) pair with minimum key."""
        if not self.root:
            return None

        node, parent = Treap._traverse(self.root, 'left')
        return node.key, node.value

    def max(self):
        """Return the (key, value) pair with maximum key."""
        if not self.root:
            return None

        node, parent = Treap._traverse(self.root, 'right')
        return node.key, node.value

    def clear(self):
        """Clear all the (key, value) pairs from the tree."""
        self.root = None

    @staticmethod
    def _traverse(node, attr, parent=None):
        while getattr(node, attr):
            node, parent = getattr(node, attr), node

        return node, parent

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


class TestTreap(unittest.TestCase):
    def setUp(self):
        self.treap = Treap()

    def test_tree(self):
        treap = self.treap
        treap[1] = 'a'
        treap[2] = 'b'
        treap[0] = 'c'
        self.assertEqual(repr(treap), repr(treap))

        self.assertEqual(treap[1], 'a')
        treap[1] = 'b'
        self.assertEqual(treap[1], 'b')
        self.assertRaises(KeyError, treap.__getitem__, 3)

        self.assertTrue(1 in treap)
        self.assertFalse(3 in treap)

        del treap[1]
        del treap[2]
        treap[1] = 'a'
        del treap[0]
        del treap[1]
        self.assertRaises(KeyError, treap.__delitem__, 1)

        treap[5] = 'a'
        treap[3] = 'b'
        treap[1] = 'c'
        treap[2] = 'd'
        treap[4] = 'e'
        treap[9] = 'f'
        treap[7] = 'g'
        treap[6] = 'h'
        treap[8] = 'i'
        self.assertEqual(treap.min(), (1, 'c'))
        self.assertEqual(treap.max(), (9, 'f'))
        treap.check()
        del treap[3]
        del treap[9]
        del treap[5]
        del treap[2]
        treap.clear()
        self.assertEqual(treap.min(), None)
        self.assertEqual(treap.max(), None)

    def test_stress(self):
        try:
            from progressbar import ProgressBar
        except ImportError:
            ProgressBar = lambda: iter

        rand = random.Random(0)
        treap = self.treap
        treap.clear()
        keys = range(10000)

        rand.shuffle(keys)
        progress = ProgressBar()
        for key in progress(keys):
            treap[key] = -1
            treap.check()

        rand.shuffle(keys)
        progress = ProgressBar()
        for key in progress(keys):
            assert key in treap

        rand.shuffle(keys)
        progress = ProgressBar()
        for key in progress(keys):
            del treap[key]
            assert key not in treap
            treap.check()


if __name__ == '__main__':
    unittest.main()
