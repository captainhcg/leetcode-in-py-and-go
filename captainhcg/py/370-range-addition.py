class Solution(object):
    def getModifiedArray(self, length, updates):
        ret = [0] * length
        for st, ed, offset in updates:
            ret[st] += offset
            if ed+1 < length:
                ret[ed+1] -= offset
        mod = 0
        for idx, v in enumerate(ret):
            mod += v
            ret[idx] = mod
        return ret
