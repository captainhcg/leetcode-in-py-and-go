class Solution(object):
    def getFactors(self, n):
        return self.helper(n, 2)

    def helper(self, n, start_from):
        ret = []
        for i in xrange(start_from, n):
            if i * i > n:
                break
            div, mod = divmod(n, i)
            if mod == 0:
                ret.append([i, div])
                for factors in self.helper(div, i):
                    ret.append([i] + factors)
        return ret
