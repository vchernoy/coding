
class Node:
    def __init__(self):
        self.next = self.prev = None
        self.key = None
        self.value = None

class LRUCache:
    def __init__(self, capacity):
        assert capacity > 0

        self.capacity = capacity
        self.table = {}
        self.size = 0
        head = Node()
        head.next = head.prev = head
        self.head = head

    def get(self, key):
        node = self.table.get(key, None)
        if node is None:
            return -1

        self._remove_node(node)
        self._add_node(node)
        return node.value

    def put(self, key, value):
        node = self.table.get(key, None)
        if node is not None:
            self._remove_node(node)
        else:
            node = Node()

        node.key = key
        node.value = value
        self._add_node(node)
        self.table[key] = node

        while self.size > self.capacity:
            node = self.head.prev
            del self.table[node.key]
            self._remove_node(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def _add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

