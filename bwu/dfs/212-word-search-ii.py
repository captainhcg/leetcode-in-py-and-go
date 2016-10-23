class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        if not board or not board[0] or not words:
            return []
        ret = set()   
        m, n = len(board), len(board[0])
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'

        for i in xrange(m):
            for j in xrange(n):
                self.dfs(ret, trie, board, i, j, '')

        return list(ret)
        
    def dfs(self, ret, trie, board, i, j, tmp):
        if '#' in trie:
            ret.add(tmp)
            
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] is None or board[i][j] not in trie:
            return
        
        char = board[i][j]
        board[i][j] = None
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            self.dfs(ret, trie[char], board, i + dx, j + dy, tmp + char)
        board[i][j] = char
