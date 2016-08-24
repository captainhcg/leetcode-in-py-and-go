class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i, h in enumerate(citations):
            if i + 1 == h:
                return h
            elif i + 1 > h:
                return i
                
        return len(citations)
