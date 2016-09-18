class Solution(object):
    def findNthDigit(self, n):
        bottom = 1
        dlen = 1
        while n > bottom * 9 * dlen:
            n -= bottom * 9 * dlen
            bottom *= 10
            dlen += 1
        num, pos = divmod(n-1, dlen)
        return int(str(bottom+num)[pos])
