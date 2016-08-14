class Solution(object):
    cache = {}
    def canWin(self, s):
        if s in self.cache:
            return self.cache[s]
            
        next_moves = self.generatePossibleNextMoves(s)
        res = False
        if not next_moves:
            res = False
        else:
            res = any(not self.canWin(next_move) for next_move in next_moves)
        self.cache[s] = res
            
        return res
        
    def generatePossibleNextMoves(self, s):
        ret = []
        for idx in xrange(len(s)):
            if s[idx:idx+2] == "++":
                ret.append(s[:idx] + "--" + s[idx+2:])
        return ret
