class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        for _ in xrange(n-1):
            new_ret = ""
            last_ch = ret[0]
            cnt = 0
            for ch in ret:
                if ch == last_ch:
                    cnt += 1
                else:
                    new_ret += str(cnt) + last_ch
                    last_ch = ch
                    cnt = 1
            new_ret += str(cnt) + last_ch
            ret = new_ret
        return ret
