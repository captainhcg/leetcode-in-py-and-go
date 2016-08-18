class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if len(self._min):
            self._min.append(min(x, self._min[-1]))
        else:
            self._min.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()
        self._min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[-1]
