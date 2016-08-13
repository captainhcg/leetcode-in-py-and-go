class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj, cnt = None, 0
        for n in nums:
            if maj is None:
                maj = n
                cnt = 1
            elif n != maj:
                cnt -= 1
                if cnt == 0:
                    maj = None
            else:
                cnt += 1
                
        return maj
