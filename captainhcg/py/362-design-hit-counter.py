from collections import deque

class HitCounter(object):
    def __init__(self):
        self.clicks = deque()
        
    def hit(self, timestamp):
        self.clicks.append(timestamp)

    def getHits(self, timestamp):
        while self.clicks and self.clicks[0] <= timestamp - 300:
            self.clicks.popleft()
        return len(self.clicks)
