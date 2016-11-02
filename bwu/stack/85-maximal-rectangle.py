class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not len(matrix[0]):
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if i > 0 and int(matrix[i][j]) > 0:
                    matrix[i][j] = int(matrix[i - 1][j]) + int(matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j])
        for i in xrange(m):
            res = max(res, self.findMaxInRow(matrix[i]))
            
        return res
        
    def findMaxInRow(self, nums):
        n = len(nums)
        l_b, r_b = [0] * n, [0] * n
        stack_l, stack_r = [], []
        max_area = 0
        for i in xrange(n):
            while stack_l and nums[stack_l[-1]] >= nums[i]:
                stack_l.pop()
            l_b[i] = -1 if not stack_l else stack_l[-1]
            stack_l.append(i)
            while stack_r and nums[stack_r[-1]] >= nums[n - 1 - i]:
                stack_r.pop()
            r_b[n - 1 - i] = n if not stack_r else stack_r[-1]
            stack_r.append(n - 1 - i)
        for i in xrange(n):
            max_area = max(max_area, (r_b[i] - l_b[i] - 1) * nums[i])
        return max_area
