class Solution(object):
    def find132pattern(self, nums):
        stack = []
        n3 = float("-inf")
        for idx in xrange(len(nums)-1, -1, -1):
            num = nums[idx]
            if num < n3:
                return True
            while stack and num > stack[-1]:
                n3 = max(stack.pop(), n3)
            stack.append(num)
        return False
