class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        x_offset = [-1, 0, 1, -1, 1, -1, 0, 1]
        y_offset = [-1, -1, -1, 0, 0, 1, 1, 1]

        def mark(x, y):
            count = 0
            for xo, yo in zip(x_offset, y_offset):
                new_x, new_y = x + xo, y + yo
                if 0 <= new_x < m and 0 <= new_y < n:
                    count += board[new_x][new_y] & 1
            
            if count < 2 or count > 3:
                pass
            elif count == 3 or board[x][y] & 1:
                board[x][y] |= 2
            
        def restore(x, y):
            board[x][y] = board[x][y] >> 1
            
        
        for x in range(m):
            for y in range(n):
                mark(x, y)
                
        for x in range(m):
            for y in range(n):
                restore(x, y)
