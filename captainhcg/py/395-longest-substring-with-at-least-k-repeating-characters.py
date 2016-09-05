class Solution(object):
    def longestSubstring(self, s, k):
        from collections import Counter
        if len(s) < k:
            return 0
        m = Counter(s)
        if all(v >= k for v in m.values()):
            return len(s)
        maxlen = idx = last_idx = 0
        for idx, ch in enumerate(s):
            if m[ch] < k:
                maxlen = max(maxlen, self.longestSubstring(s[last_idx: idx], k))
                last_idx = idx + 1
        return max(maxlen, self.longestSubstring(s[last_idx: len(s)], k))
