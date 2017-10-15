
class Solution(object):
    def __init__(self):
        self.tab = {}
    
    def generateParenthesis(self, n):
        return self.gen(n, self.tab)

    def gen(self, n, tab):
        if n == 0:
            return ['']
        
        if n in tab:
            return tab[n]

        sol = []
        for i in range(n):
            sol1 = self.gen(i, tab)
            sol2 = self.gen(n-i-1, tab)
            for s1 in sol1:
                for s2 in sol2:
                    sol.append('(' + s1 + ')' + s2)

        tab[n] = sol                    
        return sol

