class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 10:
            return []
         
        res = []   
        
        for i in xrange(num + 1):
            hours, minutes = set(), set()
            self.represent(4, i, 0, 0, hours)
            self.represent(6, num - i, 0, 0, minutes)
            
            for h in hours:
                if h >= 12:
                    continue
                h = str(h)
                for m in minutes:
                    if m >= 60:
                        continue
                    if m < 10:
                        m = '0' + str(m)
                    else:
                        m = str(m)
                    res.append(h+':'+m)
        return res
            
        
    def represent(self, n, m, start, tmp, res):
        if not m:
            res.add(tmp)
            return
        if m > n or start >= n:
            return
        for i in xrange(start, n):
            self.represent(n, m - 1, i + 1, tmp ^ (1 << i), res)
