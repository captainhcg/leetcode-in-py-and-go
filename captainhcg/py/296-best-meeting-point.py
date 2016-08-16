class Solution(object):
    def minTotalDistance(self, grid):
        xarr = []
        yarr = []
        for y in xrange(len(grid)):
            for x in xrange(len(grid[0])):
                if grid[y][x] == 1:
                    xarr.append(x)
                    yarr.append(y)
        xarr.sort()
        def getSum(arr):
            l = 0
            r = len(arr)-1
            s = 0
            while l < r:
                s += arr[r] - arr[l]
                l += 1
                r -= 1
            return s
            
        return getSum(xarr) + getSum(yarr)
