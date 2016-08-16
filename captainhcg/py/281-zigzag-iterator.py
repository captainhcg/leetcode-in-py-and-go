from collections import deque
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.queue = deque()
        for v in (v1, v2):
            if v:
                self.queue.append((v, 0))

    def next(self):
        l, idx = self.queue.popleft()
        if idx + 1 < len(l):
            self.queue.append((l, idx+1))
        return l[idx]

    def hasNext(self):
        return bool(self.queue)
