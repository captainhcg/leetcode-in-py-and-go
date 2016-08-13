class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        newstack = []
        while self.stack:
            newstack.append(self.stack.pop())
        val = newstack.pop()
        while newstack:
            self.stack.append(newstack.pop())
        return val

    def peek(self):
        """
        :rtype: int
        """
        newstack = []
        while self.stack:
            newstack.append(self.stack.pop())
        val = newstack[-1]
        while newstack:
            self.stack.append(newstack.pop())
        return val

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack
