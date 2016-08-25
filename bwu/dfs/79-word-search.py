class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
        if word is None or len(word) == 0:
            return True
            
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word):
                        return True

        return False
        
    def dfs(self, board, i, j, target):
        if len(target) == 0:
            return True
            
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or target[0] != board[i][j]:
            return False
            
        board[i][j] = '*'
        res = self.dfs(board, i + 1, j, target[1:]) or \
            self.dfs(board, i - 1, j, target[1:]) or \
            self.dfs(board, i, j + 1, target[1:]) or \
            self.dfs(board, i, j - 1, target[1:])
            
        board[i][j] = target[0]
        return res
