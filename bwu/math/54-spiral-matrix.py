class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ret = []
        self.printHelper(ret, matrix, 0, n - 1, 0, m - 1)
        return ret
        
    def printHelper(self, ret, matrix, lb, rb, ub, db):
        if lb > rb or db < ub:
            return
        elif lb == rb and db == ub:
            ret.append(matrix[lb][ub])
        elif db == ub:
            for i in xrange(lb, rb + 1):
                ret.append(matrix[ub][i])
        elif lb == rb:
            for i in xrange(ub, db + 1):
                ret.append(matrix[i][rb])
        else:
            for i in xrange(lb, rb):
                ret.append(matrix[ub][i])
            for i in xrange(ub, db):
                ret.append(matrix[i][rb])
            for i in xrange(rb, lb, -1):
                ret.append(matrix[db][i])
            for i in xrange(db, ub, -1):
                ret.append(matrix[i][lb])
            self.printHelper(ret, matrix, lb + 1, rb - 1, ub + 1, db - 1)
