class Solution(object):
    def countDigitOne(self, n):
        if n < 0:
            return 0
        s = str(n)
        cnt = 0
        for offset, ch in enumerate(s[::-1]):
            cnt += (n / (10**(offset + 1))) * (10**offset)
            if ch <= "1":
                cnt += (int(s[-offset-1:]) - 10**offset + 1) * int(ch)
            else:
                cnt += 10**offset
        return cnt
