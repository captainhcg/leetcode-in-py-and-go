class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(nums, cmp = lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y)))
        return str(int(''.join(map(str,nums))))
