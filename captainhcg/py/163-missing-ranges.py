class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        arr = []
        def append(lo, hi):
            if lo == hi:
                arr.append(str(lo))
            else:
                arr.append("%s->%s" % (lo, hi))
        
        last_seen = None
        for n in nums:
            if n < lower or n > upper:
                continue
            if last_seen is None:
                if n != lower:
                    append(lower, n-1)
            elif n == last_seen + 1:
                pass
            else:
                append(last_seen+1, n-1)
            last_seen = n
            
        if last_seen is None:
            append(lower, upper)
        elif last_seen != upper:
            append(last_seen + 1, upper)
            
        return arr
