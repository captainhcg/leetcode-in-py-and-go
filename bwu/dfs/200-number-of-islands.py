class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return res
            
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, m, n, i, j)
        return res
        
    def dfs(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
            
        grid[i][j] = '0'
        self.dfs(grid, m, n, i + 1, j)
        self.dfs(grid, m, n, i - 1, j)
        self.dfs(grid, m, n, i, j + 1)
        self.dfs(grid, m, n, i, j - 1)
