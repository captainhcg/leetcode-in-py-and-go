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
        median = self.findMedian()
        if len(self.l_heap) == len(self.r_heap):
            if median is None or num <= median:
                heapq.heappush(self.l_heap, -num)
            else:
                tmp = heapq.heappushpop(self.r_heap, num)
                heapq.heappush(self.l_heap, -tmp)
        else:
            if num <= median:
                tmp = heapq.heappushpop(self.l_heap, -num)
                heapq.heappush(self.r_heap, -tmp)
            else:
                heapq.heappush(self.r_heap, num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not len(self.l_heap) and not len(self.r_heap):
            return None
        elif not len(self.r_heap):
            return -self.l_heap[0] * 1.0
            
        if len(self.l_heap) == len(self.r_heap):
            return (self.r_heap[0] - self.l_heap[0]) / 2.0
        else:
            return -self.l_heap[0] * 1.0
