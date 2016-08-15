import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = None
    
    def balance(self):
        lmin, lmax = len(self.min_heap), len(self.max_heap)
        if lmin > lmax + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif lmax > lmin:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
    def setMedian(self):
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            self.median = float(self.min_heap[0] - self.max_heap[0]) / 2
        else:
            self.median = float(self.min_heap[0])
            
    def addNum(self, num):
        if self.median is None:
            heapq.heappush(self.min_heap, num)
        else:
            if num > self.median:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        self.balance()
        self.setMedian()

    def findMedian(self):
        return self.median
