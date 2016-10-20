class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
            
        res = []
        curr = []
        curr_len = 0
        for word in words:
            if curr_len + len(curr) + len(word) > maxWidth:
                for i in xrange(maxWidth - curr_len):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                res.append(''.join(curr))
                curr, curr_len = [], 0
            curr.append(word)
            curr_len += len(word)
            
        return res + [' '.join(curr).ljust(maxWidth)]
