class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        m = dict()
        l, r, counter = 0, 0, 0
        maxlen = 0
        while r < len(s):
            ch = s[r]
            m[ch] = m.get(ch, 0) + 1
            if m[ch] == 1:
                counter += 1
            if counter <= 2 and r - l + 1 > maxlen:
                maxlen = r - l + 1
            while counter >= 3:
                ch = s[l]
                m[ch] -= 1
                if m[ch] == 0:
                    counter -= 1
                l += 1
            r += 1
        return maxlen
