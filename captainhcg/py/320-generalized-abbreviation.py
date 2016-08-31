class Solution(object):
    def generateAbbreviations(self, word):
        ret = []
        for n in xrange(2 ** len(word)):
            offset = 0
            cnt = 0
            s = []
            while offset < len(word):
                if ((1 << offset) & n):  # number
                    cnt += 1
                else:  # char
                    if cnt > 0:
                        s.append(str(cnt))
                        cnt = 0
                    s.append(word[offset])
                offset += 1
            if cnt > 0:
                s.append(str(cnt))
            ret.append("".join(s))
        return ret
        
