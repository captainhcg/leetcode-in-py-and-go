class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(height)
        if n < 2:
            return res
            
        l, r = 0, n - 1
        while l < r:
            res = max(res, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
