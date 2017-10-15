
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda e: e.end)
        r = self.F(intervals)
        return len(intervals) - r
        
    def F(self, ivs):
        sol = [ivs[0]]
        for iv in ivs[1:]:
            if not self.overlaps(sol[-1], iv):
                sol.append(iv)
                
        return len(sol)
        
    def overlaps(self, iv1, iv2):
        l = max(iv1.start, iv2.start)
        h = min(iv1.end, iv2.end)
        return l < h

