
def compute(A):
    n = len(A)
    maxA = [0] * n
    maxA[-1] = A[-1]
    for i in xrange(n-2, -1, -1):
        maxA[i] = max(A[i], maxA[i+1])

    # for i=0..n-1, maxA[i] == max(A[i:])

    stocks = 0
    money = 0
    for i in xrange(n):
        if (stocks > 0) and (A[i] == maxA[i]):
            # sell all the stocks for $A[i]:
            stocks = 0
        elif (i < n-1) and (A[i] < maxA[i+1]):
            # buy 1 stock for $A[i]:
            stocks += 1
            money += maxA[i+1] - A[i]

    assert(money >= 0)

    return money

for t in xrange(int(raw_input())):
    n = int(raw_input())
    A = [int(w) for w in raw_input().split()]
    assert(len(A) == n)
    for i in xrange(n):
        assert(A[i] >= 0)


    print compute(A)
