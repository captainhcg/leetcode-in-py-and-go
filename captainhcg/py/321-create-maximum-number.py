class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def prep(nums, length):
            arr = []
            drop = len(nums) - length
            for n in nums:
                while drop and arr and n > arr[-1] and drop:
                    arr.pop()
                    drop -= 1
                arr.append(n)
            return arr[:length]
    
        def merge(a, b):
            from collections import deque
            _a = deque(a)
            _b = deque(b)
            return [max(_a, _b).popleft() for _ in xrange(len(a) + len(b))]
    
        return max(merge(prep(nums1, n), prep(nums2, k-n)) for n in xrange(k+1) if len(nums1) >= n and len(nums2) >= k-n )
