class Solution(object):
    def repeatedSubstringPattern(self, str):
        for l in xrange(1, (len(str) >> 1) + 1):
            if len(str) % l == 0 and len(str) / l * (str[:l]) == str:
                    return True
        return False
