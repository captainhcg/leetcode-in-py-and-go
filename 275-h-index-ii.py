class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not len(citations):
            return 0
        ret = 0
        left, right = 0, len(citations) - 1
        while left <= right:
            md = (left + right) / 2
            if citations[md] == len(citations) - md:
                return citations[md]
            elif citations[md] > len(citations) - md:
                ret = max(ret, len(citations) - md)
                right = md - 1
            else:
                ret = max(ret, citations[md])
                left = md + 1
        return ret
