class Solution(object):
    def exist(self, board, word):
        if not word:
            return True
            
        rows = len(board)
        cols = len(board[0])
            
        def dfs(y, x, idx):
            if board[y][x] != word[idx]:
                return False
            elif idx == len(word) - 1:
                return True
            ori = board[y][x]
            board[y][x] = "."
            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                yy, xx = y + oy, x + ox
                if 0 <= yy < rows and 0 <= xx < cols:
                    if dfs(yy, xx, idx + 1):
                        return True
            board[y][x] = ori
            return False
        
        for y in xrange(rows):
            for x in xrange(cols):
                if dfs(y, x, 0):
                    return True
        
        return False
