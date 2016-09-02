class Solution(object):
    def findStrobogrammatic(self, n):
        if n & 1:
            slen = 1
            ret = ['8', '1', '0']
        else:
            slen = 0
            ret = ['']
        while slen < n:
            new_ret = []
            slen += 2
            for s in ret:
                new_ret.append("6" + s + "9")
                new_ret.append("8" + s + "8")
                new_ret.append("1" + s + "1")
                new_ret.append("9" + s + "6")
                if slen < n:
                    new_ret.append("0" + s + "0")
            ret = new_ret
        return ret
