class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        cnt = 0
        blds = []
        visited = []
        ret = -1
        big_cnt = {}
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    cnt += 1
                    blds.append([(i, j)])
                    visited.append(set((i, j)))
        step = 0
        found = False
        
        while sum(len(b) for b in blds):
            step += 1
            for i in xrange(cnt):
                for _ in xrange(len(blds[i])):
                    c_x, c_y = blds[i].pop(0)
                    for d_x, d_y in (0, 1), (0, -1), (1, 0), (-1, 0):
                        n_x, n_y = c_x + d_x, c_y + d_y
                        if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] <= 0 and (n_x, n_y) not in visited[i]:
                            visited[i].add((n_x, n_y))
                            blds[i].append((n_x, n_y))
                            grid[n_x][n_y] -= step
                            if (n_x, n_y) not in big_cnt:
                                big_cnt[(n_x, n_y)] = 1
                            else:
                                big_cnt[(n_x, n_y)] += 1
                            if big_cnt[(n_x, n_y)] == cnt:
                                if ret == -1:
                                    ret = -grid[n_x][n_y]
                                else:
                                    ret = min(ret, -grid[n_x][n_y])
                
        return ret
