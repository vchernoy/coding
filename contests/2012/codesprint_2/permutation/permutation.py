import random, time

def print_perm(A):
    for x in A:
        print x,

    print


def random_perm(V):
    P = [-1] * len(V)
    cost = 0
    Set = range(len(V))
    m = len(Set)

    for j in xrange(len(V)):
        m -= 1
        i = random.randint(0, m)
        e = Set[i]
        Set[i] = Set[m]
        P[j] = e
        cost += V[P[j-1]][e] if j > 0 else 0

    return (P, cost)


def generated_perm(V):
    end_time = time.time() + 15

    best_P, best_cost = random_perm(V)
    while time.time() < end_time:
        for i in xrange(100):
            P, cost = random_perm(V)
            if cost > best_cost:
                best_cost = cost
                best_P = P

    return best_P

V = []
for i in xrange(int(raw_input())):
    V.append([int(w) for w in raw_input().split()])

random.seed()

print_perm(generated_perm(V))

