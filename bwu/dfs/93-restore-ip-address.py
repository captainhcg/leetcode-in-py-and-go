class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        ret = []
        if n > 12:
            return ret
            
        self.helper(s, 0, 4, [], ret)
        return ret
        
    def helper(self, s, curr, level, tmp, ret):
        if level == 0 and curr == len(s):
            ret.append('.'.join(tmp))
            return
    
        if curr < len(s) and s[curr] == '0':
            self.helper(s, curr + 1, level - 1, tmp + ['0'], ret)
        else:
            for i in xrange(1, 4):
                if curr + i <= len(s) and 0 <= int(s[curr: curr + i]) <= 255:
                    self.helper(s, curr + i, level - 1, tmp + [s[curr: curr + i]], ret)
                
