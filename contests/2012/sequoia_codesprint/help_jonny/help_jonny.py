
for i in xrange(int(raw_input())):
    n = int(raw_input())

    print 'YES' if (n >= 4) and (n % 4 in [0, 1]) else 'NO'
