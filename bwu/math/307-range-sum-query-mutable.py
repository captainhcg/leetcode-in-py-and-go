class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        n = len(self.nums)
        self.bit = [0] * (n + 1)
        for i in xrange(1, n + 1):
            self.build(i, self.nums[i - 1])

    def build(self, i, val):
        while i <= len(self.nums):
            self.bit[i] += val
            i += i & (-i)
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        self.build(i + 1, delta)

    def getSum(self, i):
        ret = 0
        while i:
            ret += self.bit[i]
            i -= i & (-i)
        return ret
    
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self.getSum(i)
