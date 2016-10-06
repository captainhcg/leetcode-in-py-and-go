# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
            
        buckets = []
        for intv in intervals:
            buckets.append((intv.start, intv.start))
            buckets.append((intv.end, -intv.start))
            
        buckets.sort()
        rooms = 1
        ret = rooms
        for i in xrange(1, len(buckets)):
            if buckets[i][1] >= 0:
                rooms += 1
                ret = max(ret, rooms)
            elif buckets[i][1] < 0:
                rooms -= 1
                
        return ret
