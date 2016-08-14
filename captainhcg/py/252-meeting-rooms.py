class Solution(object):
    def canAttendMeetings(self, intervals):
        last_end = -1
        intervals.sort(key=lambda i: (i.start, i.end))
        for i in intervals:
            if i.start < last_end:
                return False
            last_end = i.end
        return True
