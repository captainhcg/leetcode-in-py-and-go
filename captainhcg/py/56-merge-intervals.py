class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda i: (i.start, i.end))
        last_start, last_end = intervals[0].start, intervals[0].end
        ret = []
        for i in intervals[1:]:
            st, ed = i.start, i.end
            if st <= last_end:
                last_end = max(last_end, ed)
            else:
                ret.append([last_start, last_end])
                last_start, last_end = st, ed
        ret.append([last_start, last_end])
        return ret
