class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        l = 0
        for n in nums:
            if n in d:
                continue
            else:
                left = right = n
                if (n - 1) in d:
                    left = d[n-1][0]
                if (n + 1) in d:
                    right = d[n+1][1]
                if right - left + 1 > l:
                    l = right - left + 1
                d[left] = d[right] = d[n] = (left, right)
        return l
