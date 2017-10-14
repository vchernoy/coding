
n, q = [int(w) for w in raw_input().split()]
a = int(raw_input(), 2)
b = int(raw_input(), 2)
res = []
for i in xrange(q):
    cmd = raw_input().split()
    if cmd[0] == 'set_a':
        idx, x = int(cmd[1]), int(cmd[2])
        if x:
            a |= 1 << idx
        else:
            a &= ~(1 << idx)
    elif cmd[0] == 'set_b':
        idx, x = int(cmd[1]), int(cmd[2])
        if x:
            b |= 1 << idx
        else:
            b &= ~(1 << idx)
    elif cmd[0] == 'get_c':
        idx = int(cmd[1])
        c = a + b
        bit = c & (1 << idx)
        res.append('1' if bit else '0')
    else:
        assert(False)

print ''.join(res)

