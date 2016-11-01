class Solution(object):
    def findRightInterval(self, intervals):
        import bisect
        intervals_list = sorted((inv.start, idx) for idx, inv in enumerate(intervals))
        ret = []
        for idx, inv in enumerate(intervals):
            offset = bisect.bisect_left(intervals_list, (inv.end, -1))
            if offset == len(intervals):
                ret.append(-1)
            else:
                ret.append(intervals_list[offset][1])
        return ret
