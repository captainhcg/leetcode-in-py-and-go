class Solution(object):
    def wordPatternMatch(self, pattern, str):
        def dfs(idx, s, worddict, wordset):
            if idx == len(pattern) and not s:
                return True
            elif idx >= len(pattern) or not s:
                return False

            ch = pattern[idx]
            if ch in worddict:
                pat = worddict[ch]
                if s.startswith(pat):
                    return dfs(idx + 1, s[len(pat):], worddict, wordset)
                else:
                    return False
            else:
                for jdx in xrange(1, len(s) + 1):
                    pat = s[:jdx]
                    if pat in wordset:
                        continue
                    worddict[ch] = pat
                    wordset.add(pat)
                    if dfs(idx + 1, s[len(pat):], worddict, wordset):
                        return True
                    wordset.remove(pat)
                    del worddict[ch]
            return False

        return dfs(0, str, dict(), set())
