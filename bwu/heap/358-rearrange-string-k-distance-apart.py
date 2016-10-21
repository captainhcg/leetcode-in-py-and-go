class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        heap = [(-freq, char) for char, freq in collections.Counter(str).items()]
        heapq.heapify(heap)
        res = []
        
        if k == 0:
            return str
        
        while len(res) < len(str):
            tmp = []
            for _ in xrange(k):
                if len(res) == len(str):
                    return ''.join(res)
                if not heap:
                    return ''
                freq, curr = heapq.heappop(heap)
                res.append(curr)
                if freq < -1:
                    tmp.append((freq + 1, curr))
            while tmp:
                heapq.heappush(heap, tmp.pop())
        return ''.join(res)
