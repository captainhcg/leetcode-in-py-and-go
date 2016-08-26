class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
            
        from_s = set([beginWord])
        from_e = set([endWord])
        
        cnt = 2
        while from_s:
            next_level = set([])
            for word in from_s:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in from_e:
                            return cnt
                        if new_word != word and new_word in wordList:
                            next_level.add(new_word)
                            wordList.remove(new_word)
            
            if len(next_level) < len(from_e):
                from_s, from_e = next_level, from_e
            else:
                from_e, from_s = next_level, from_e
            cnt += 1
            
        return 0
