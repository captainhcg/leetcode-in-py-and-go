class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        tmap = {}
        for ch in t:
            tmap[ch] = tmap.get(ch, 0) + 1
        minlen, counter = len(s) + 1, len(t)
        mins = None
        l, r = 0, 0
        while r < len(s):
            ch = s[r]
            if ch in tmap:
                tmap[ch] = tmap[ch] - 1
                if tmap[ch] >= 0:
                    counter -= 1
            while counter == 0:
                if r - l + 1 < minlen:
                    minlen, mins = r - l + 1, s[l:r + 1]
                ch = s[l]
                if ch in tmap:
                    tmap[ch] += 1
                    if tmap[ch] > 0:
                        counter += 1
                l += 1
            r += 1
        return mins or ""
