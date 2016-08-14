class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows <= 0:
            return ret
            
        for i in xrange(numRows):
            level = [1]
            if i == 1:
                level.append(1)
            if i > 1:
                for j in xrange(1, len(ret[-1])):
                    level.append(ret[-1][j - 1] + ret[-1][j])
                level.append(1)
            ret.append(level)
            
        return ret
