class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or not numRows:
            return ''
        if numRows == 1:
            return s
            
        n = len(s)
        res = ''
        rows = ['' for _ in xrange(numRows)]
        idx, direction = 0, -1
        for c in s:
            if idx == 0 or idx == numRows - 1:
                direction *= -1
            rows[idx] += c
            idx += 1 * direction
         
        for row in rows:
            res += row
            
        return res
