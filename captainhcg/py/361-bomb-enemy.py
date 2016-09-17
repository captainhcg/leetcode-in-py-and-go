class Solution(object):
    def maxKilledEnemies(self, grid):
        matRow = [[None] * len(grid[0]) for _ in xrange(len(grid))]
        matCol = [[None] * len(grid[0]) for _ in xrange(len(grid))]
        
        def checkRow(row, col):
            count = 0
            l = r = col
            while l >= 0:
                if grid[row][l] == 'W':
                    break
                elif grid[row][l] == 'E':
                    count += 1
                l -= 1
            while r < len(grid[0]):
                if grid[row][r] == 'W':
                    break
                elif grid[row][r] == 'E':
                    count += 1
                r += 1
            for x in xrange(l+1, r):
                matRow[row][x] = count

        def checkCol(row, col):
            count = 0
            u = d = row
            while u >= 0:
                if grid[u][col] == 'W':
                    break
                elif grid[u][col] == 'E':
                    count += 1
                u -= 1
            while d < len(grid):
                if grid[d][col] == 'W':
                    break
                elif grid[d][col] == 'E':
                    count += 1
                d += 1
            for y in xrange(u+1, d):
                matCol[y][col] = count
        
        blank = []
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if grid[row][col] == "0":
                    blank.append((row, col))
                    if matRow[row][col] is None:
                        checkRow(row, col)
                    if matCol[row][col] is None:
                        checkCol(row, col)
        
        _max = 0
        for row, col in blank:
            _max = max(_max, (matRow[row][col] or 0) + (matCol[row][col] or 0))
        return _max
