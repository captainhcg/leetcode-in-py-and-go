class Solution(object):
    def minMeetingRooms(self, intervals):
        arr = []
        for i in intervals:
            arr.append((i.start, 1))
            arr.append((i.end, 0))
        arr.sort()
        global_max = 0
        rooms = 0
        for idx, tp in arr:
            rooms = rooms + 1 if tp == 1 else rooms - 1
            global_max = max(global_max, rooms)
        return global_max
