class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = []
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                heapq.heappush(h, matrix[i][j])
        
        for i in xrange(k - 1):
            heapq.heappop(h)
        return heapq.heappop(h)
