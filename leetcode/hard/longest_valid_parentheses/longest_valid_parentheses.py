
class Solution(object):
    def longestValidParentheses(self, s):
        r1 = self.longest(s)
        r2 = self.longest(self.rev(s))
        return max(r1, r2)

    def rev(self, s):
        res = []
        for i in xrange(len(s)-1, -1, -1):
            c = s[i]
            if c == '(':
                res.append(')')
            else:
                res.append('(')
                
        return ''.join(res)

    def longest(self, s):
        n = len(s)
        r = 0
        i = 0
        while i < n - r:
            if s[i] == ')':
                i += 1
                continue

            r2 = self.valid(s, i)
            r = max(r, r2)
            i += r2
            if i < n and s[i] == '(':
                break

        return r
        
    def valid(self, s, beg):
        n = len(s)
        k = 0
        counter = 0
        i = beg
        while i < n:
            c = s[i]
            if c == '(':
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    k = i - beg + 1
                elif counter < 0:
                    return k
                    
            i += 1

        return k

