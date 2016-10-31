class Solution(object):
    def countBattleships(self, board):
        if not board or not board[0]:
            return 0
        row = len(board)
        col = len(board[0])
        num_x = num_dot = 0
        for y in xrange(0, row):
            for x in xrange(0, col):
                if board[y][x] == "X":
                    num_x += 1
                    for _y, _x in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
                        if _x < 0 or _x >= col or _y < 0 or _y >= row:
                            num_dot += 1
                        elif board[_y][_x] == '.':
                            num_dot += 1
        return (num_dot - num_x * 2) / 2
                
