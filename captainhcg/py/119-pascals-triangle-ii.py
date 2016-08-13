class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in xrange(1, rowIndex+1):
            for idx in xrange(len(row)-1, 0, -1):
                row[idx] = row[idx] + row[idx-1]
            row.append(1)
        return row
