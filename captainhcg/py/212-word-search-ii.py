class Solution(object):
    def findWords(self, board, words):
        if not board or not board[0]:
            return []
        
        root = {}
        def make_trie(word, idx, parent):
            if idx >= len(word):
                parent["#"] = True
                return
            ch = word[idx]
            if ch not in parent:
                parent[ch] = {}
            make_trie(word, idx + 1, parent[ch])
            
        for w in words:
            make_trie(w, 0, root)
        
        ret = []
        visited = set()
        def dfs(cur, y, x, parent):
            if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
                return
            if (y, x) in visited:
                return
            ch = board[y][x]
            if ch not in parent:
                return
            parent = parent[ch]
            cur = cur + ch
            if parent.get("#"):
                ret.append(cur)
                parent["#"] = False 
            visited.add((y, x))
            for oy, ox in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(cur, y+oy, x+ox, parent)
            visited.remove((y, x))
        
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                dfs("", row, col, root)
        
        return ret
