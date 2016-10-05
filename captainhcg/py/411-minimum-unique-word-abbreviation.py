class Solution(object):
    def minAbbreviation(self, target, dictionary):
        from itertools import combinations
        dictionary = [w for w in dictionary if len(w) == len(target)]
        if not dictionary:
            return str(len(target))

        def notdup(com):
            for w in dictionary:
                if all(w[idx] == target[idx] for idx in com):
                    return False
            return True

        def ret(com):
            com = [-1] + com + [len(target)]
            s = ""
            for idx in xrange(1, len(com)):
                p = com[idx]
                if p - com[idx - 1] > 1:
                    s += str(p - com[idx - 1] - 1)
                if p < len(target):
                    s += target[p]
            return s

        nums = range(len(target))
        if len(nums) > 1:
            nums[1], nums[-1] = nums[-1], nums[1]
        for p in xrange(1, len(target) + 1):
            for com in combinations(nums, p):
                if notdup(com):
                    return ret(sorted(com))
