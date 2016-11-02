# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.start = 0
        self.cnt = 0
        self.buf4 = [''] * 4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if self.start == 0:
                self.cnt = read4(self.buf4)
            if self.cnt == 0:
                break
            while idx < n and self.start < self.cnt:
                buf[idx] = self.buf4[self.start]
                idx += 1
                self.start += 1
            if self.start >= self.cnt:
                self.start = 0
        return idx
