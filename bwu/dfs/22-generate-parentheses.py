class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()
        self.dfs(['('] * n, [')'] * n, '', res)
        return list(res)
        
    def dfs(self, left, right, tmp, res):
        if not len(left) and not len(right) and tmp not in res:
            res.add(tmp)
        elif not len(left) and len(right):
            self.dfs([], right[: -1], tmp + ')', res)
        elif len(left) <= len(right):
            self.dfs(left[: -1], right, tmp + '(', res)
            self.dfs(left, right[: -1], tmp + ')', res)
