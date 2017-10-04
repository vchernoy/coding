
class Solution(object):
    def removeInvalidParentheses(self, s):
        res1 = self.remove(s)
        res2 = self.remove(self.rev(s))
        res1.update({self.rev(e) for e in res2})
        
        return [r for r in res1]
        
    def rev(self, s):
        n = len(s)
        r = []
        for i in range(n-1, -1, -1):
            c = s[i]
            if c == '(':
                r.append(')')
            elif c == ')':
                r.append('(')
            else:
                r.append(c)
                
        return ''.join(r)
        
    def remove(self, s):
        n = len(s)
        keep = [True] * n
        stack = []
        for i in range(n):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    keep[i] = False
                    
        for j in stack:
            keep[j] = False
            
        res = set()
        self.gen(res, s, keep)
        return res
        
    def gen(self, res, s, keep):
        n = len(s)
        s1 = self.to_str(keep, s)
        if s1 in res:
            return
        
        res.add(s1)
        
        for i in range(n):
            if keep[i]:
                continue
            keep[i] = True
            c = s[i]
            if c == ')':
                for j in range(i-1, -1, -1):
                    if not keep[j]:
                        continue
                    c0 = s[j]
                    if c0 == ')':
                        keep[j] = False
                        self.gen(res, s, keep)
                        keep[j] = True
            elif c == '(':
                for j in range(i+1, n, +1):
                    if not keep[j]:
                        continue
                    c0 = s[j]
                    if c0 == '(':
                        keep[j] = False
                        self.gen(res, s, keep)
                        keep[j] = True
            keep[i] = False
                
    def to_str(self, keep, s):
        n = len(s)
        return ''.join([s[i] for i in range(n) if keep[i]])
        
        
    # ())v)(()(((((())
    #   x xx  xxxx
    # () v  ()    (())
    #   (v) ()    (())

    # ())v)(()(((((())
    # (  v)(()     ())       ????
    #  xx     xxxxx

    # ())v)(()(((((())
    #   x x   xxxxx
    # () v (()     ())

    # ())v)
    #  ()v
    #   (v)
    
    # (()(((((())
    #  ()(())
    # (()())

