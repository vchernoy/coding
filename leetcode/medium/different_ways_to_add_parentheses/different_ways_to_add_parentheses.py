
class Solution(object):
    def diffWaysToCompute(self, input):
        expr = ['']
        for c in input:
            if c in '+-*':
                expr[-1] = int(expr[-1])
                expr.append(str(c))
                expr.append('')
            else:
                expr[-1] = expr[-1] + c
                
        expr[-1] = int(expr[-1])

        return self.ways(expr)
        
    def ways(self, expr):
        if len(expr) == 1:
            return [expr[0]]

        sol = []
        for i in range(1, len(expr)-1, 2):
            op = expr[i]
            sol1 = self.ways(expr[:i])
            sol2 = self.ways(expr[i+1:])
            for s1 in sol1:
                for s2 in sol2:
                    if op == '+':
                        s = s1 + s2
                    elif op == '-':
                        s = s1 - s2
                    elif op == '*':
                        s = s1 * s2
                        
                    sol.append(s)
                    
        return sol

