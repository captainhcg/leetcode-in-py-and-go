class Solution(object):
    def solveSudoku(self, board):
        mask = sum((1 << offset) for offset in xrange(9))

        def get_mask(n, mask):
            if n != '.' and mask & (1 << (ord(n) - 49)):
                mask -= 1 << (ord(n) - 49)
            return mask

        def get_available_numbers(row, col):
            new_mask = mask
            for n in board[row]:
                new_mask = get_mask(n, new_mask)

            for r in board:
                new_mask = get_mask(r[col], new_mask)

            for offset_y in xrange(3):
                for offset_x in xrange(3):
                    new_mask = get_mask(board[row / 3 * 3 + offset_y][col / 3 * 3 + offset_x], new_mask)
            return [n + 1 for n in xrange(9) if new_mask & (1 << n)]

        def check(row, col):
            if row == 9:
                return True

            if col < 8:
                next_col, next_row = col + 1, row
            else:
                next_col, next_row = 0, row + 1

            if board[row][col] != '.':
                return check(next_row, next_col)

            for n in get_available_numbers(row, col):
                board[row][col] = str(n)
                if check(next_row, next_col):
                    return True
                board[row][col] = '.'

            return False

        check(0, 0)
