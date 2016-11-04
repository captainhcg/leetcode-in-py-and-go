class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.cap = size
        self.sum = 0
        self.queue = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sum += val
        if self.cap > 0:
            self.cap -= 1
        else:
            self.sum -= self.queue.pop(0)
        return self.sum * 1.0 / len(self.queue)
