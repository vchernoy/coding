
import heapq

class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        heapq.heappush(self.min_heap, num)
        while self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)
            
        while abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) < len(self.max_heap):
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappop(self.max_heap)
            else:                
                heapq.heappush(self.max_heap, -self.min_heap[0])
                heapq.heappop(self.min_heap)

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) * 0.5
            
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
            
        return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

