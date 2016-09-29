# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        intervals.sort(key=lambda i: (i.start, i.end))
        for i in intervals:
            start, end = i.start, i.end
            if not ret:
                ret.append((start, end))
            else:
                last_s, last_e = ret.pop()
                if last_e >= start:
                    ret.append((last_s, max(end, last_e)))
                else:
                    ret.append((last_s, last_e))
                    ret.append((start, end))
        return ret
        
