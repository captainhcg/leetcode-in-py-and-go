class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum = []
        for idx, n in enumerate(nums):
            if idx == 0:
                self.sum.append(n)
            else:
                self.sum.append(n + self.sum[idx-1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sum[j]
        else:
            return self.sum[j] - self.sum[i-1]
