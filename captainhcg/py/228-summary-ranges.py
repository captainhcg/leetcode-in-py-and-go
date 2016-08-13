class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        if not nums:
            return []
        last_st = last_n = nums[0]
        for n in nums[1:]:
            if n == last_n + 1:
                last_n += 1
            else:
                if last_st == last_n:
                    ret.append(str(last_st))
                else:
                    ret.append("{}->{}".format(last_st, last_n))
                last_st = n
                last_n = n
        if last_st == last_n:
            ret.append(str(last_st))
        else:
            ret.append("{}->{}".format(last_st, last_n))
        return ret
