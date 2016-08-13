class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [""]
        for _ in xrange(1, n+1):
            newres = []
            for r in res:
                newres.append("0" + r)
            for r in res[::-1]:
                newres.append("1" + r)
            res = newres
        return [int(r, 2) for r in res]
        
