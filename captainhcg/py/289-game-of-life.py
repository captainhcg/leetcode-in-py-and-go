class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        x_offsets = [-1, -1, -1, 0, 0, 1, 1, 1]
        y_offsets = [-1, 0, 1, -1, 1, -1, 0, 1]
        def mark(y, x):
            cnt = 0
            for y_offset, x_offset in zip(x_offsets, y_offsets):
                newy, newx = y + y_offset, x + x_offset
                if 0 <= newy < M and 0 <= newx < N:
                    cnt += board[newy][newx] & 1
            if cnt < 2 or cnt > 3:
                pass
            elif board[y][x] & 1 or cnt == 3:
                board[y][x] = board[y][x] | 2

        def restore(y, x):
            board[y][x] = board[y][x] >> 1

        for y in xrange(M):
            for x in range(N):
                mark(y, x)

        for y in xrange(M):
            for x in range(N):
                restore(y, x)
