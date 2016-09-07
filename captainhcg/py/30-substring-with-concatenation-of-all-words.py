class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        wlen = len(words[0])
        wmap = {}
        ret = []
        for word in words:
            wmap[word] = wmap.get(word, 0) + 1
        for idx in xrange(wlen):
            l = r = idx
            while l <= len(s) - len(words) * wlen:
                nmap = {}
                cnt = 0
                while cnt < len(words):
                    r = l + cnt * wlen
                    new_word = s[r: r + wlen]
                    if new_word not in wmap:
                        l = r
                        break
                    else:
                        nmap[new_word] = nmap.get(new_word, 0) + 1
                        if nmap[new_word] > wmap[new_word]:
                            break
                        else:
                            cnt += 1
                            if cnt == len(words):
                                ret.append(l)
                l = l + wlen
        return ret
