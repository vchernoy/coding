
class Solution:
    def change(self, amount, coins):
        coins = [coin for coin in coins if coin <= amount]
        tab = {}
        def _change(amount, n):
            if amount == 0:
                return 1
    
            if amount < 0 or n == 0:
                return 0
        
            # amount > 0 and n > 0
            key = (amount, n)
            r = tab.get(key)
            if r is not None:
                return r
    
            r = 0
            for i in range(n):
                r += _change(amount - coins[i], i+1)
    
            tab[key] = r    
            return r

        return _change(amount, len(coins))

