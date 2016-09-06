class Solution(object):
    def reverseWords(self, s):
        def reverse(sidx, eidx):
            while sidx < eidx:
                s[sidx], s[eidx] = s[eidx], s[sidx]
                sidx += 1
                eidx -= 1

        reverse(0, len(s) - 1)
        word_start = 0

        for idx, ch in enumerate(s):
            if ch[0] == " ":
                reverse(word_start, idx - 1)
                word_start = idx + 1
            elif idx == len(s) - 1:
                reverse(word_start, idx)
