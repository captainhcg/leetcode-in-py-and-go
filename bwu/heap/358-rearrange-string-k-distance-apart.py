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
        
        while len(res) < len(str):
            if not heap:
                return ''
            tmp = []
            freq, curr = heapq.heappop(heap)
            res.append(curr)
            for _ in xrange(k - 1):
                if len(res) == len(str):
                    return ''.join(res)
                if not heap:
                    return ''
                next_freq, next_v = heapq.heappop(heap)
                res.append(next_v)
                if next_freq < -1:
                    tmp.append((next_freq + 1, next_v))
            while tmp:
                heapq.heappush(heap, tmp.pop())
            if freq < -1:
                heapq.heappush(heap, (freq + 1, curr))
        return ''.join(res)
                
