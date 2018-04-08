
def solve(d, p):
    shoots = []
    i = 0
    for c in p:
        if c == 'S':
            shoots.append(i)
        else:
            i += 1

    m = len(shoots)
    if m > d:
        return -1

    damage = sum(2**i for i in shoots)
    if damage <= d:
        return 0

    hacks = 0
    while damage > d:
        hacks += 1
        for i in range(m-1, -1, -1):
            if i == 0:
                if shoots[0] > 0:
                    shoots[0] -= 1
                    damage -= 2**shoots[0]
                    break
            else:
                if shoots[i-1] < shoots[i]:
                    shoots[i] -= 1
                    damage -= 2**shoots[i]
                    break

    return hacks


def main():
    for t in range(int(input())):
        tokens = input().split()
        d, p = int(tokens[0]), tokens[1]
        r = solve(d, p)
        if r == -1:
            print("Case #{}: IMPOSSIBLE".format(t+1))
        else:
            print("Case #{}: {}".format(t+1, r))

main()
