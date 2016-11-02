class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        if not num:
            return results
        for i in xrange(len(num)):
            if len(str(int(num[:i + 1]))) != i + 1:
                continue
            self.dfs(num[i + 1:], target, int(num[:i + 1]), int(num[:i + 1]), num[:i + 1], results)
        return results
        
    def dfs(self, num, target, val, diff, tmp, results):
        if len(num) == 0 and target == val:
            results.append(tmp)
        else:
            for i in xrange(len(num)):
                curr = int(num[:i + 1])
                if len(str(curr)) != i + 1:
                    continue
                self.dfs(num[i + 1:], target, val + curr, curr, tmp + '+' + num[:i + 1], results)
                self.dfs(num[i + 1:], target, val - curr, -curr, tmp + '-' + num[:i + 1], results)
                self.dfs(num[i + 1:], target, val - diff + (diff * curr), diff * curr, tmp + '*' + num[:i + 1], results)
