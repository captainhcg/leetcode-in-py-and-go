from heapq import *

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num):
        heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0])
