
class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        tab = {}
        def _change(amount, n):
            if amount == 0:
                return 0

            if amount < 0 or n == 0:
                return -1

            # amount > 0 and n > 0
            key = (amount, n)
            r = tab.get(key)
            if r is not None:
                return r

            r = -1
            for i in range(n-1,-1,-1):
                if r >= 0:
                    r1 = (amount - 1) / coins[i]
                    if r1 >= r:
                        break

                r0 = _change(amount - coins[i], i+1)
                if r0 >= 0:
                    r = min(r, r0) if r >= 0 else r0

            if r >= 0:
                r += 1

            tab[key] = r
            return r

        return _change(amount, len(coins))

