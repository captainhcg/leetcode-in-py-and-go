class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        arr = [str(i) for i in nums]
        arr.sort(cmp=self.cmp)
        return ("".join(arr)).lstrip("0") or "0"

    def cmp(self, a, b):
        if a + b > b + a:
            return -1
        return 1
