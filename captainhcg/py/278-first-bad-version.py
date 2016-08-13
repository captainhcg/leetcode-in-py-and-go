# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        higher = n
        while lower != higher:
            to_check = (lower + higher) / 2
            ret = isBadVersion(to_check)
            if ret:
                if to_check == lower + 1:
                    if isBadVersion(lower):
                        return lower
                    return to_check
                else:
                    if isBadVersion(to_check-1):
                        higher = to_check - 1
                    else:
                        return to_check
            else:
                lower = to_check + 1
        return lower
