class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        if s.isdigit():
            return True
        try:
            n = float(s)
            return True
        except:
            pass
        return False
