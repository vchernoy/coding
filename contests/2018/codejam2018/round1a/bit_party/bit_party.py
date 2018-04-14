
INF = 10**25


def solve(n_robots, bits_to_buy, n_cashiers, max_items_per_customer, time_to_scan_item, handling_payment_time):
    def best_time(r, b, c):
        if b == 0:
            return 0

        if r == 0 or c == 0:
            return INF

        r = min(r, c)
        key = (r, b, c)
        if key in tab:
            return tab[key]

        m, s, p = max_items_per_customer[c - 1], time_to_scan_item[c - 1], handling_payment_time[c - 1]

        best_time_spent = best_time(r, b, c - 1)

        for bits in range(1, min(b, m)+1):
            cashier_time_spent = bits * s + p
            others_time_spent = best_time(r - 1, b - bits, c - 1)
            time_spent = max(cashier_time_spent, others_time_spent)
            best_time_spent = min(best_time_spent, time_spent)
            if cashier_time_spent >= others_time_spent:
                break

        tab[key] = best_time_spent

        return best_time_spent

    tab = {}

    return best_time(n_robots, bits_to_buy, n_cashiers)


def main():
    for t in range(int(input())):
        n_robots, bits_to_buy, n_cashiers = [int(w) for w in input().split()]
        max_items_per_customer, time_to_scan_item, handling_payment_time = [], [], []
        for i in range(n_cashiers):
            m, s, p = [int(w) for w in input().split()]
            max_items_per_customer.append(m)
            time_to_scan_item.append(s)
            handling_payment_time.append(p)

        res = solve(n_robots, bits_to_buy, n_cashiers, max_items_per_customer, time_to_scan_item, handling_payment_time)
        print("Case #{}: {}".format(t+1, res))

main()
