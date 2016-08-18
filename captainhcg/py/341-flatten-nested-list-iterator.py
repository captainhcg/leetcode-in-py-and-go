class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.stack.extend(nestedList[::-1])

    def next(self):
        val = self.stack[-1].getInteger()
        self.stack.pop()
        return val
        
    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            self.stack.extend(self.stack.pop().getList()[::-1])
        return False
