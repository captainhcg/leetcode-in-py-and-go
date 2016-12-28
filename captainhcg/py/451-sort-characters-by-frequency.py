class Solution(object):
    def frequencySort(self, s):
        ctr = collections.Counter(s)
        heap = []
        for ch, cnt in ctr.iteritems():
            heapq.heappush(heap, (-cnt, ch))
        arr = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            arr.append(ch * -cnt)
        return "".join(arr)
