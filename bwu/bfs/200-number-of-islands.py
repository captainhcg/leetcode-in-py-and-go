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
                    self.bfs(grid, m, n, i, j)
        return res
        
    def bfs(self, grid, m, n, i, j):
        delta_x = [-1, 1, 0, 0]
        delta_y = [0, 0, -1, 1]
        queue = [(i, j)]
        grid[i][j] = '0'
        while queue:
            x, y = queue.pop(0)
            for dx, dy in zip(delta_x, delta_y):
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == '1':
                    queue.append((x + dx, y + dy))
                    grid[x + dx][y + dy] = '0'
