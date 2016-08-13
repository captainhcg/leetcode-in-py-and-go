class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.start_set = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.map:
            return
        left = right = val
        if (val-1) in self.map:
            left = self.map[val-1][0]
        else:
            self.start_set.add(left)
            
        if (val+1) in self.map:
            right = self.map[val+1][1]
            self.start_set.remove(val+1)
        self.map[val] = self.map[left] = self.map[right] = (left, right)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        starts = sorted(self.start_set)
        ret = []
        for s in starts:
            ret.append(list(self.map[s]))
        return ret
