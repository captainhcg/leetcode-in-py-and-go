class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1, self.queue2 = [], []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1.pop(0)
        
        while len(self.queue2):
            self.queue1.append(self.queue2.pop(0))

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0
