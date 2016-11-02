class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda o: (o.end, o.start))
        last_end = float('-inf')
        to_remove = 0
        for inv in intervals:
            st, ed = inv.start, inv.end
            if st < last_end:
                to_remove += 1
            else:
                last_end = ed
        return to_remove
