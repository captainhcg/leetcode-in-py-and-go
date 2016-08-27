class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
        
        ret = []
        if not digits:
            return ret
            
        self.dfs(digits, '', mapping, ret)
        return ret
        
    def dfs(self, digits, curr, mapping, ret):
        if not digits:
            ret.append(curr)
            return
        
        for c in mapping[digits[0]]:
            self.dfs(digits[1:], curr + c, mapping, ret)
