from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l_heap = []
        self.r_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.l_heap, -heappushpop(self.r_heap, num))
        if len(self.r_heap) < len(self.l_heap):
            heappush(self.r_heap, -heappop(self.l_heap))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.r_heap) > len(self.l_heap):
            return float(self.r_heap[0])
        else:
            return (self.r_heap[0] - self.l_heap[0]) / 2.0
