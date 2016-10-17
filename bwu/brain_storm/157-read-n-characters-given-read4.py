# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
            
        tmp = [''] * 4
        number = min(n, read4(tmp))
        ans = number
        buf[:number] = tmp[:number]
        while number == 4:
            number = min(read4(tmp), n - ans)
            buf[ans: ans+number] = tmp[:number]
            ans += number
            
        return ans
