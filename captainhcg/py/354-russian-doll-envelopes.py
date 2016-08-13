class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        from bisect import bisect_left as select
        envelopes.sort(key=lambda (x, y): (x, -y))
        res = []
        for _, h in envelopes:
        	if not res or h > res[-1]:
        		res.append(h)
        	else:
        		to_replace = select(res, h)
        		res[to_replace] = h
        return len(res)
