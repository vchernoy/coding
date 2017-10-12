#!/Users/slava/work/codejam2017/env/py3/bin/python

import heapq
import time


def flips(src, nbits, k):
    dst = to_int([1] * nbits)
    if src == dst:
        return 0

    mask = to_int([1] * k)

    nsteps = 1
    visited = set()
    visited.add(src)
    stacks = [[src], []]
    while stacks[0]:
        for v in stacks[0]:
            edge = mask
            for i in range(0, nbits - k+1):
                u = v ^ edge
                if u not in visited:
                    if u == dst:
                        return nsteps

                    visited.add(u)
                    stacks[1].append(u)

                edge *= 2

        stacks = [stacks[1], []]
        nsteps += 1

        if nsteps > nbits:
            break

    return "IMPOSSIBLE"


def count_bits(bits):
    k = 0
    for b in bits:
        k += b

    return k


def n1bits(n):
    r = 0
    while n > 0:
        r += n % 2
        n //= 2

    return r


def flips2(src_bits, k):
    nbits = len(src_bits)
    src = to_int(src_bits)
    dst = to_int([1] * nbits)
    if src == dst:
        return 0

    seq = 0

    mask = to_int([1] * k)

    visited = set()
    visited.add(src)

    pq = []
    heapq.heappush(pq, ((nbits - n1bits(src) + k - 1) // k, 0, seq, src))
    seq += 1
    while pq:
        _, nsteps, _, v = heapq.heappop(pq)

        nsteps += 1

        if nsteps > nbits:
            continue

        edge = mask
        for i in range(0, nbits - k+1):
            u = v ^ edge
            if u not in visited:
                if u == dst:
                    return nsteps

                visited.add(u)
                heapq.heappush(pq, ((nbits - n1bits(u)+k-1) // k + nsteps, nsteps, seq, u))
                seq += 1

            edge *= 2

    return "IMPOSSIBLE"




class Node:
    def __init__(self, bits, val=None, n0bits=None):
        self.bits = bits
        self.val = val
        self.n0bits = n0bits
        if val is None:
            self.val = to_int(bits)

        if n0bits is None:
            self.n0bits = len(bits) - count_bits(bits)


def flips1(src_bits, k):
    nbits = len(src_bits)
    src = Node(src_bits)
    dst = Node([1] * nbits)
    if src.val == dst.val:
        return 0

    seq = 0

    visited = set()
    visited.add(src.val)

    pq = []
    heapq.heappush(pq, ((src.n0bits+k-1) // k, 0, seq, src))
    seq += 1
    while pq:
        _, nsteps, _, v = heapq.heappop(pq)

        bits = list(v.bits)
        for i in range(k-1):
            bits[i] = 1 - bits[i]

        for i in range(k-1, nbits):
            bits[i] = 1 - bits[i]
            if i >= k:
                bits[i-k] = 1 - bits[i-k]

            u = Node(bits)
            if u.val not in visited:
                if u.val == dst.val:
                    return nsteps + 1

                bits = list(bits)

                visited.add(u.val)
                heapq.heappush(pq, ((u.n0bits+k-1) // k + nsteps+1, nsteps+1, seq, u))
                seq += 1

    return "IMPOSSIBLE"


def to_int(bits):
    n = 0
    for b in bits:
        n = n * 2 + b

    return n


def to_bits(n, nbits):
    bits = [0] * nbits
    i = nbits-1
    while n > 0:
        bits[i] = n % 2
        n //= 2
        i -= 1
    return bits


if 0:
    nbits = 10
    total_time0 = 0
    total_time1 = 0
    for k in range(2, nbits):
        for n in range(2**nbits):
            bits = to_bits(n, nbits)
            assert(to_int(bits) == n)
            t0 = time.monotonic()
            res0 = flips(n, len(bits), k)
            t1 = time.monotonic()
            res1 = flips1(bits, k)
            t2 = time.monotonic()
            assert(res0 == res1)

            total_time0 += t1-t0
            total_time1 += t2-t1

    print(total_time0, total_time1)

    print("passed")

for test in range(int(input())):
    s, k = input().split()
    k = int(k)
    bits = [1 if c == '+' else 0 for c in s]
    n = to_int(bits)
    # res = flips(n, len(bits), k)
    # print("Case #{}: {}".format(test+1, res))

    res = flips2(bits, k)
    print("Case #{}: {}".format(test+1, res))
