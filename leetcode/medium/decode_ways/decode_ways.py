
class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0

        onedigit = [str(k) for k in xrange(1,10)]
        twodigit = [str(k) for k in xrange(10,27)]
        
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1 if s[0] in onedigit else 0
        
        for i in xrange(2,n+1):
            f[i] = f[i-1] if s[i-1] in onedigit else 0
            f[i] += f[i-2] if s[i-2:i] in twodigit else 0
        
        return f[n]

