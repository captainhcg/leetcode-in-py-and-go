class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        h = []
        for n1 in nums1:
            for n2 in nums2:
                s = -(n1 + n2)
                if len(h) < k:
                    heapq.heappush(h, (s, (n1, n2)))
                else:
                    if s <= h[0][0]:
                        break
                    heapq.heappop(h)
                    heapq.heappush(h, (s, (n1, n2)))
        return [p[1] for p in h]
