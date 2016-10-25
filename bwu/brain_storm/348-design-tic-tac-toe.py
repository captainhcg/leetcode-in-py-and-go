class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = [0] * 2

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.row[row] += (1 if player == 1 else -1)
        self.col[col] += (1 if player == 1 else -1)
        
        if row == col:
            self.diag[0] += (1 if player == 1 else -1)
        if row + col == self.n - 1:
            self.diag[1] += (1 if player == 1 else -1)
            
        if max(self.row[row], self.col[col], self.diag[0], self.diag[1]) == self.n:
            return 1
        elif min(self.row[row], self.col[col], self.diag[0], self.diag[1]) == -self.n:
            return 2
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
