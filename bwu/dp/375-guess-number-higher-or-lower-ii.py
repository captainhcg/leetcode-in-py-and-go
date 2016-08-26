class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for _ in xrange(n + 1)] for _ in xrange(n + 1)]
            
        def dp(table, s, e):
            if s >= e:
                return 0
                
            if table[s][e] != 0:
                return table[s][e]
                
            res = float('inf')
            for i in xrange(s, e + 1):
                tmp = i + max(dp(table, s, i - 1), dp(table, i + 1, e))
                res = min(res, tmp)
                
            table[s][e] = res
            return table[s][e]
            
        return dp(table, 1, n)
