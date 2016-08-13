class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        clist = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]
        for idx in digits:
            idx_num = int(idx)
            new_res = []
            for next_char in clist[idx_num]:
                for prefix in res:
                    new_res.append(prefix + next_char)
            res = new_res
        return res
