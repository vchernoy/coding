
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        tab = set()
        res = set()
        for i in range(0, len(s)-10+1):
            dna = s[i:i+10]
            if dna in tab:
                res.add(dna)
            else:
                tab.add(dna)
        
        return [dna for dna in res]

