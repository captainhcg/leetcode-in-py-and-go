class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, N = 0, len(citations) - 1, len(citations)
        while left <= right:
            md = (left + right) >> 1
            if citations[md] == N - md:
                return citations[md]
            elif citations[md] > N - md:
                right = md - 1
            else:
                left = md + 1
        return N - (right + 1)
        
