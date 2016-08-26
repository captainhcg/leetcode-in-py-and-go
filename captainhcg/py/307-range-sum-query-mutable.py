class NumArray(object):
    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.bit = [0] * (len(nums) + 1)
        for idx, n in enumerate(nums):
            self.update(idx, n)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        idx = i + 1
        while idx <= len(self.nums):
            self.bit[idx] += diff
            idx += idx & (-idx)

    def sumRange(self, i, j):
        def getSum(idx):
            cnt = 0
            while idx:
                cnt += self.bit[idx]
                idx -= idx & (-idx)
            return cnt
        return getSum(j + 1) - getSum(i)
