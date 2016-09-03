class Solution(object):
    cache = {0: [''], 1: ['0', '1', '8']}
    def strobogrammaticInRange(self, low, high):
        cnt = 0
        for n in xrange(len(low), len(high) + 1):
            res = [s for s in self.helper(n) if s == "0" or s[0] != "0"]
            if n == len(low) == len(high):
                cnt += len([s for s in res if high >= s >= low])
            elif n == len(low):
                cnt += len([s for s in res if s >= low])
            elif n == len(high):
                cnt += len([s for s in res if s <= high])
            else:
                cnt += len(res)
        return cnt

    def helper(self, n):
        if n not in self.cache:
            ret = []
            for s in self.helper(n-2):
                ret.append("6" + s + "9")
                ret.append("8" + s + "8")
                ret.append("1" + s + "1")
                ret.append("9" + s + "6")
                ret.append("0" + s + "0")
            self.cache[n] = ret
        return self.cache[n]
