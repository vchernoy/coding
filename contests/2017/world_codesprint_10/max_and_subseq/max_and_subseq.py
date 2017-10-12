import sys

N_BITS = 60
M = 10**9+7


def inv(x):
    return pow(x, M-2, M)


factorials = [1] * (10**5+10)
inv_factorials = [1] * (10**5+10)
for i in range(2, len(factorials)):
    factorials[i] = (factorials[i-1] * i) % M

factorials = tuple(factorials)

for i in range(len(factorials)):
    inv_factorials[i] = inv(factorials[i])

inv_factorials = tuple(inv_factorials)

def fact(x):
    return factorials[x]


def binom(n, k):
    # return (fact(n) * inv(fact(k)) * inv(fact(n-k))) % M

    return (factorials[n] * inv_factorials[k] * inv_factorials[n-k]) % M


class NilNode:
    def __init__(self):
        self.__dict__['n'] = 0

    def get0(self):
        return NIL

    def get1(self):
        return NIL

    def __setattr__(self, key, value):
        assert(0)

NIL = NilNode()


class Node:
    def __init__(self):
        self.n = 0
        self.bit0 = None
        self.bit1 = None

    def add(self, bits):
        self.n += 1
        cur = self
        for i in range(len(bits)-1, -1, -1):
            b = bits[i]
            cur = cur._bit1() if b else cur._bit0()
            cur.n += 1

    def _bit0(self):
        if self.bit0 is None:
            self.bit0 = Node()

        return self.bit0

    def _bit1(self):
        if self.bit1 is None:
            self.bit1 = Node()

        return self.bit1

    def get0(self):
        return self.bit0 if self.bit0 else NIL

    def get1(self):
        return self.bit1 if self.bit1 else NIL

    def merge(self, node):
        node0 = node.get0()
        if node0.n > 0:
            if self.n == 0:
                self.bit0 = node0
            else:
                self._bit0().merge(node0)

        node1 = node.get1()
        if node1.n > 0:
            if self.n == 0:
                self.bit1 = node1
            else:
                self._bit1().merge(node1)

        self.n += node.n

        node.bit0 = node.bit1 = None
        node.n = 0


def to_bits(x):
    bits = [0] * N_BITS
    i = 0
    while x > 0:
        bits[i] = x % 2
        x //= 2
        i += 1

    return tuple(bits)


def to_int(bits):
    x = 0
    for i in range(len(bits)-1, -1, -1):
        x *= 2
        x += bits[i]

    return x


def n_bits(x):
    k = 0
    while x > 0:
        x //= 2
        k += 1

    return max(k,1)


def solve(n, k, a):
    global N_BITS

    a.sort(reverse=False)

    # max_a = max(a)
    max_a = a[-1]
    # max_a = a[0]
    N_BITS = min(N_BITS, n_bits(max_a))

    root = Node()
    for x in a:
        root.add(to_bits(x))

    assert root.n == n

    cur = root
    bits = [0] * N_BITS
    i = len(bits)-1
    while i >= 0:
        # print(i)
        assert cur.n >= k

        cur1 = cur.get1()
        n1 = cur1.n
        if n1 >= k:
            bits[i] = 1
            cur.bits0 = None
            cur = cur1
        else:
            if n1 > 0:
                cur._bit0().merge(cur1)

            cur.bits1 = None
            cur = cur.get0()

        i -= 1

    # print(bits, to_int(bits))
    # print(cur.n, k, binom(cur.n, k))

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
    result = solve(n, k, a)
    print(result)
    sys.exit(0)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
result = solve(n, k, a)
print ("\n".join(map(str, result)))


