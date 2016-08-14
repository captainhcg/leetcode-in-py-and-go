class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n1 = self.step(n)
        n2 = self.step(n1)
        
        while n1 != 1:
            if n1 == n2:
                return False
            else:
                n1 = self.step(n1)
                n2 = self.step(n2)
                n2 = self.step(n2)
        return True
        
    def step(self, n):
        result = 0
        while n:
            result += pow(n % 10, 2)
            n = n / 10
        return result
