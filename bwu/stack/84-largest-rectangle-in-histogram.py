class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
            
        result = 0
        n = len(heights)
        if n == 1:
            return heights[0]
        r_b, l_b = [0] * n, [0] * n
        stack_r, stack_l = [], []
        for i in xrange(n):
            while stack_r and heights[stack_r[-1]] >= heights[i]:
                stack_r.pop()
            if not stack_r:
                r_b[i] = -1
            else:
                r_b[i] = stack_r[-1]
            stack_r.append(i)
            
            while stack_l and heights[stack_l[-1]] >= heights[n - 1 - i]:
                stack_l.pop()
            if not stack_l:
                l_b[n - i - 1] = n
            else:
                l_b[n - i - 1] = stack_l[-1]
            stack_l.append(n - 1 - i)

        for i in xrange(n):
            result = max(result, (l_b[i] - r_b[i] - 1) * heights[i])
        return result
