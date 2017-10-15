
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def flatten(self, nestedList):
        res = []
        def f(l):
            for x in l:
                if x.isInteger():
                    res.append(x.getInteger())
                else:
                    f(x.getList())
        
        f(nestedList)
        return res
        
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = self.flatten(nestedList)
        self.cur = 0

    def next(self):
        """
        :rtype: int
        """
        val = self.res[self.cur]
        self.cur+=1
        return val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.res)
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

