from collections import deque

class Stack(object):
    def __init__(self):
        self.queue = deque()
        
    def push(self, x):
        self.queue.append(x)

    def _get_top(self, remove=False):
        tmp = deque()
        last = None
        while self.queue:
            last = self.queue.popleft()
            tmp.append(last)
        while tmp:
            ele = tmp.popleft()
            if remove and ele == last:
                break
            self.queue.append(ele)
        return last
        
    def pop(self):
        return self._get_top(remove=True)
        
    def top(self):
        return self._get_top(remove=False)
        
    def empty(self):
        return not bool(self.queue)
