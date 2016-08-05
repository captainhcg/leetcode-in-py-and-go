# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, higher = 1, n
        myguess = (1 + n) / 2
        ret = guess(myguess)
        while ret != 0:
            if ret == -1:
                higher = myguess - 1
            else:
                lower = myguess + 1
            myguess = (lower + higher)/2 
            ret = guess(myguess)
        return myguess
