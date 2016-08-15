class Solution(object):
    def firstMissingPositive(self, nums):
        idx, length = 0, len(nums)
        while idx < length:
            n = nums[idx]
            if n <= 0 or n > length or n - 1 == idx:
                pass
            else:
                should_be_at = n - 1
                if nums[idx] != nums[should_be_at]:
                    nums[should_be_at], nums[idx] = nums[idx], nums[should_be_at]
                    continue
            idx += 1

        for idx, n in enumerate(nums):
            if n - 1 != idx:
                return idx + 1

        return length + 1
