from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0
        
    def next(self, val):
        if len(self.queue) >= self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return float(self.total) / len(self.queue)
