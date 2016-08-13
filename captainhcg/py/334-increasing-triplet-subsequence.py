class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = second = float("inf")
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second:
                second = n
            else:
                return True
        return False
