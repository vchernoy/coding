import sys

N_BITS = 60
M = 10**9+7

factorials = [1] * (10**5+10)
for i in range(2, len(factorials)):
    factorials[i] = (factorials[i-1] * i) % M


def fact(x):
    return factorials[x]


def inv(x):
    return pow(x, M-2, M)


def binom(n, k):
    return (fact(n) * inv(fact(k)) * inv(fact(n-k))) % M


class Node:
    def __init__(self):
        self.n = 0
        self.bits = None

    def add(self, bits):
        self.n += 1
        cur = self
        for i in range(len(bits)-1, -1, -1):
            b = bits[i]
            cur = cur.bit(b)
            cur.n += 1

    def bit(self, b):
        if self.bits is None:
            self.bits = [None, None]

        if self.bits[b] is None:
            self.bits[b] = Node()

        return self.bits[b]

    def get(self, b):
        if self.bits is None or self.bits[b] is None:
            return NIL

        return self.bits[b]

    def merge(self, node):
        if node.n == 0:
            return

        if self.n == 0:
            self.n = node.n
            self.bits = node.bits
            node.bits = None
            return

        self.n += node.n
        self.bit(0).merge(node.get(0))
        self.bit(1).merge(node.get(1))


NIL = Node()


def to_bits(x):
    bits = [0] * N_BITS
    i = 0
    while x > 0:
        bits[i] = x % 2
        x //= 2
        i += 1

    return bits


def to_int(bits):
    x = 0
    for i in range(len(bits)-1, -1, -1):
        x *= 2
        x += bits[i]

    return x


def n_bits(x):
    k = 1
    while x > 0:
        x //= 2
        k += 1

    return k


def solve0(n, k, a):
    global N_BITS

    a.sort(reverse=True)

    max_a = max(a)
    N_BITS = min(N_BITS, n_bits(max_a))

    root = Node()
    for x in a:
        y = to_bits(x)
        #print(y, x, to_int(y))
        #assert to_int(y) == x
        root.add(y)
        #if root.n % 10000 == 0:
        #    print(root.n)

    assert root.n == n

    cur = root
    bits = [0] * N_BITS
    i = len(bits)-1
    while i >= 0:
        assert cur.n >= k
        cur1 = cur.get(1)
        n1 = cur1.n
        if n1 >= k:
            bits[i] = 1
            cur = cur1
        else:
            cur.bit(0).merge(cur1)
            cur.bits[1] = None
            cur = cur.get(0)

        i -= 1

    print(bits, to_int(bits))
    print(cur.n, k, binom(cur.n, k))

    return to_int(bits), binom(cur.n, k)

if 1:
    import random
    random.seed(4)
    a = [0] * (10**5)
    n = len(a)
    for i in range(len(a)):
        a[i] = random.randint(10**17, 10**18)

    k = random.randint(2,n-1)

    # a = [2,4,8]
    # k = 3
    # n = len(a)

    print(n, k, sum(a) % M)
    result = solve0(n, k, a)
    print(result)
    sys.exit(0)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
result = solve0(n, k, a)
print ("\n".join(map(str, result)))


