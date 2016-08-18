class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._sums = [0]
        for n in nums:
            self._sums.append(self._sums[-1] + n)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self._sums[j + 1]
        else:
            return self._sums[j + 1] - self._sums[i]
