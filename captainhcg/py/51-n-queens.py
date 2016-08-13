class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.board = [["."] * n for _ in xrange(n)]
        self.ret = []
        self.helper(0)
        return self.ret

    def get_res(self):
        arr = []
        for a in self.board:
            arr.append("".join(a))
        self.ret.append(arr)

    def check_valid(self, y, x):
        def _check(yy, xx):
            if 0 <= yy < self.n and 0 <= xx < self.n:
                return self.board[yy][xx] == '.'
            else:
                return True

        for idx in xrange(0, self.n):
            if not _check(idx, x):
                return False
            if not _check(y-idx, x-idx):
                return False
            if not _check(y-idx, x+idx):
                return False
        return True

    def helper(self, level):
        for idx in xrange(self.n):
            if self.check_valid(level, idx):
                self.board[level][idx] = 'Q'
                if level == self.n - 1:
                    self.get_res()
                    self.board[level][idx] = '.'
                    return
                else:
                    self.helper(level+1)
                    self.board[level][idx] = '.'
