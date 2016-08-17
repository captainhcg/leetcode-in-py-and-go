class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = '1'
        for _ in xrange(n - 1):
            last_ch = ret[0]
            count = 0
            new_ret = ''
            for c in ret:
                if c == last_ch:
                    count += 1
                else:
                    new_ret += str(count) + last_ch
                    last_ch = c
                    count = 1
                    
            new_ret += str(count) + last_ch
            ret = new_ret
            
        return ret
