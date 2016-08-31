class Solution(object):
    def insert(self, intervals, newInterval):
        ret = []
        idx = 0
        while idx < len(intervals):
            if intervals[idx].end < newInterval.start:
                ret.append(intervals[idx])
                idx += 1
            else:
                break

        while idx < len(intervals):
            if intervals[idx].start <= newInterval.end:
                newInterval.start = min(intervals[idx].start, newInterval.start)
                newInterval.end = max(intervals[idx].end, newInterval.end)
                idx += 1
            else:
                break
        ret.append(newInterval)

        while idx < len(intervals):
            ret.append(intervals[idx])
            idx += 1

        return ret
