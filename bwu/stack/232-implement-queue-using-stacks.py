class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack1) == 0:
            return None
        
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        
        self.stack2.pop()
        
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack1) == 0:
            return None
        
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        
        res = self.stack2[-1]
        
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
            
        return res
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.stack1) == 0
