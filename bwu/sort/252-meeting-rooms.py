# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        bucket = []
        for intv in intervals:
            bucket.append((intv.start, intv.end))
            
        bucket.sort()
        for i in xrange(1, len(bucket)):
            if bucket[i][0] < bucket[i - 1][1]:
                return False
        return True
