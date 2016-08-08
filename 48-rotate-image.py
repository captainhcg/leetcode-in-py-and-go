class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        to_mat = zip(*matrix[::-1])
        for idx in xrange(len(matrix)):
            for jdx in xrange(len(matrix[0])):
                matrix[idx][jdx] = to_mat[idx][jdx]
