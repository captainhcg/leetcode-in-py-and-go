class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        odd_options = ['0', '1', '8']
        even_options = ['00', '11', '88', '69', '96']
        if n == 1:
            return odd_options
        if n == 2:
            return even_options[1:]
        if n % 2:
            pre, inserts = self.findStrobogrammatic(n - 1), odd_options
        else:
            pre, inserts = self.findStrobogrammatic(n - 2), even_options
        mid = (n - 1) / 2
        return [p[:mid] + i + p[mid:] for i in inserts for p in pre]
