
def solve(values, n):
    values0 = [values[i] for i in range(n) if i % 2 == 0]
    values0.sort()
    values1 = [values[i] for i in range(n) if i % 2 == 1]
    values1.sort()
    trouble_sorted_values = tuple(values0[i // 2] if i % 2 == 0 else values1[i // 2] for i in range(n))
    for i in range(n-1):
        if trouble_sorted_values[i] > trouble_sorted_values[i+1]:
            return i

    return -1


def main():
    for t in range(int(input())):
        n = int(input())
        values = tuple(int(w) for w in input().split())

        r = solve(values, n)
        if r == -1:
            print("Case #{}: OK".format(t+1))
        else:
            print("Case #{}: {}".format(t+1, r))

main()
