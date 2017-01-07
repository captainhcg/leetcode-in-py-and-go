class Solution(object):
    def makesquare(self, nums):
        from collections import Counter
        d = Counter(nums)
        total = sum(nums)
        if total <= 0 or total % 4 != 0:
            return False
        width = total / 4
        l = [[k, v] for k, v in d.iteritems()]

        def dfs(st, _sum, cnt):
            for idx in xrange(st, len(l)):
                k, v = l[idx]
                if v == 0 or _sum + k > width:
                    continue
                l[idx][1] -= 1
                if _sum + k == width:
                    if cnt + 1 == 4:
                        return True
                    if dfs(0, 0, cnt + 1) is True:
                        return True
                if dfs(idx, _sum + k, cnt) is True:
                    return True
                l[idx][1] += 1
            return False

        return dfs(0, 0, 0)
