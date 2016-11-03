class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValid(val):
            cnt, tmp = 0, 0
            for n in nums:
                tmp += n
                if tmp > val:
                    cnt +=1
                    if cnt >= m:
                        return False
                    tmp = n
            return True
            
        left, right = max(nums), sum(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if isValid(mid):
                right = mid
            else:
                left = mid
                
        if isValid(left):
            return left
        else:
            return right
