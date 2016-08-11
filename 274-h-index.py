class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        cnt = h = 0
        for n in citations:
            if n < h + 1:
                return h
            cnt += 1
            if h + 1 <= cnt and h + 1 <= n:
                h = h + 1
        return h
