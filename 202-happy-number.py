class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            new_n = sum(int(d)**2 for d in str(n))
            if new_n == 1:
                return True
            elif new_n in seen:
                return False
            seen.add(new_n) 
            n = new_n
