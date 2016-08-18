class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for l in nestedList[::-1]:
            self.stack.append(l)

    def next(self):
        val = self.stack[-1].getInteger()
        self.stack.pop()
        return val
        
    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            ele = self.stack.pop()
            for e in ele.getList()[::-1]:
                self.stack.append(e)
        return False
