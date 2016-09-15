class Solution(object):
    def rearrangeString(self, str, k):
        import heapq
        from collections import Counter
        k = max(k, 1)
        ret = []
        heap = list((-v, ch) for ch, v in Counter(str).iteritems())
        heapq.heapify(heap)
        
        while True:
            temp = []
            cnt = k
            while cnt and heap:
                cnt -= 1
                v, ch = heapq.heappop(heap)
                ret.append(ch)
                if v + 1 < 0:
                    temp.append((v + 1, ch))
            
            if cnt != 0:
                break
            
            for v, ch in temp:
                heapq.heappush(heap, (v, ch))

        return "".join(ret) if len(ret) == len(str) else ""
