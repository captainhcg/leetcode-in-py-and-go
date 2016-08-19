class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        m = [0] * 128
        l, r, counter = 0, 0, 0
        maxlen = 0
        while r < len(s):
            ch = ord(s[r])
            m[ch] = m[ch] + 1
            if m[ch] == 1:
                counter += 1
            if counter <= k and r - l + 1 > maxlen:
                maxlen = r - l + 1
            while counter > k:
                ch = ord(s[l])
                m[ch] -= 1
                if m[ch] == 0:
                    counter -= 1
                l += 1
            r += 1
        return maxlen
