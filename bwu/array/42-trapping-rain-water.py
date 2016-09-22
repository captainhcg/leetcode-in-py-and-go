class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
            
        leftMax, rightMax = [0] * n, [0] * n
        maxL = height[0]
        maxR = height[-1]
        for i in xrange(1, n):
            maxL = max(height[i - 1], maxL)
            leftMax[i] = maxL
            maxR = max(height[n - i], maxR)
            rightMax[n - i - 1] = maxR
            
        ret = 0

        for i in xrange(1, n - 1):
            currH = min(leftMax[i], rightMax[i])
            if currH > height[i]:
                ret += currH - height[i]
                
        return ret
