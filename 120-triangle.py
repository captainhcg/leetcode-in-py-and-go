class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        mat = []
        for _ in xrange(len(triangle)):
            mat.append([0] * len(triangle))
            
        for x in xrange(len(triangle)):
            for y in xrange(len(triangle[x])):
                if x == 0:
                    mat[0][0] = triangle[0][0]
                elif y == 0:
                    mat[x][0] = mat[x-1][0] + triangle[x][y]
                elif y == x:
                    mat[x][y] = mat[x-1][y-1] + triangle[x][y]
                else:
                    mat[x][y] = min(mat[x-1][y], mat[x-1][y-1]) + triangle[x][y]
        return min(mat[-1])
