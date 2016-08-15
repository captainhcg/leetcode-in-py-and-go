class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in xrange(9)]
        cols = [set() for _ in xrange(9)]
        squares = [[set() for _ in xrange(3)] for _ in xrange(3)]
        
        for x in xrange(9):
            for y in xrange(9):
                if board[x][y] == '.':
                    continue
                if board[x][y] not in rows[x] and board[x][y] not in cols[y] and board[x][y] not in squares[x / 3][y / 3]:
                    rows[x].add(board[x][y])
                    cols[y].add(board[x][y])
                    squares[x / 3][y / 3].add(board[x][y])
                else:
                    return False
        return True
