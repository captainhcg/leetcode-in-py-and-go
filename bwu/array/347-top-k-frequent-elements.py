class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        buckets = [[] for _ in nums]
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        
        for key, val in counts.items():
            buckets[val - 1].append(key)
            
        ret = []
        for i in xrange(len(nums) - 1, -1, -1):
            if len(buckets[i]) <= k - len(ret):
                ret += buckets[i]
            else:
                ret += buckets[i][:k - len(ret)]
                return ret
        return ret
