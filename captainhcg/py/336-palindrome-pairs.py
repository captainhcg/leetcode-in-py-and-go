class Solution(object):
    def palindromePairs(self, words):
        words_dict = dict((w, idx) for idx, w in enumerate(words))
        ret = set()
        for idx, w in enumerate(words):
            reversed_w = w[::-1]
            for ed in xrange(len(w) + 1):
                suffix = reversed_w[ed:]
                if suffix in words_dict and reversed_w[:ed] == reversed_w[:ed][::-1] and words_dict[suffix] != idx:
                    ret.add((idx, words_dict[suffix]))
                prefix = reversed_w[:ed]
                if prefix in words_dict and reversed_w[ed:] == reversed_w[ed:][::-1] and words_dict[prefix] != idx:
                    ret.add((words_dict[prefix], idx))
        return list(list(v) for v in ret)
