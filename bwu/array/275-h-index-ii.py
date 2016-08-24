class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
            
        n = len(citations)
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if citations[n - 1 - mid] >= mid + 1:
                l = mid
            else:
                r = mid
            
        if citations[n - 1 - r] >= r + 1:
            return r + 1
        elif citations[n - 1 - l] >= l + 1:
            return l + 1
        else:
            return 0
