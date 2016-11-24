class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        row_cnt, col_cnt = 0, [0] * n
        ret = 0
        for i in xrange(m):
            for j in xrange(n):
                if not j or grid[i][j - 1] == 'W':
                    row_cnt = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'W':
                            break
                        row_cnt += grid[i][k] == 'E'
                if not i or grid[i - 1][j] == 'W':
                    col_cnt[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == 'W':
                            break
                        col_cnt[j] += grid[k][j] == 'E'
                if grid[i][j] == '0':
                    ret = max(ret, row_cnt + col_cnt[j])
        return ret
