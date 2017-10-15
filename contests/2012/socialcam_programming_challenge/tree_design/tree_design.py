
n = int(raw_input())
tree = []
start = 1
for i in xrange(1, n+1):
    for j in xrange(1, i+4):
        tree.append('*' * start)
        start += 2

    start -= 6 if i % 2 == 0 else 4

basis = '|' * (n + 1 - n % 2)
for i in xrange(1, n+1):
    tree.append(basis)

width = max([len(row) for row in tree])
for row in tree:
    indent = ' ' * ((width - len(row)) / 2)
    print indent + row

