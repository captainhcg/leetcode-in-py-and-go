class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_arr, y_arr = [], []
        m, n = len(grid), len(grid[0]) if grid else 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    x_arr.append(i)
                    y_arr.append(j)
        return self.getMin(x_arr) + self.getMin(y_arr)
        
    def getMin(self, arr):
        arr.sort()
        l, r = 0, len(arr) - 1
        res = 0
        while l < r:
            res += arr[r] - arr[l]
            l += 1
            r -= 1
        return res
