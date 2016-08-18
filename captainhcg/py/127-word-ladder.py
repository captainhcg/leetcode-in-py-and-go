import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return 1
        friendsA = set([beginWord])
        friendsB = set([endWord])
        cnt = 2
        while friendsA:
            newfriends = set([])
            for f in friendsA:
                for idx in xrange(len(f)):
                    for ch in string.ascii_lowercase:
                        newword = f[:idx] + ch + f[idx + 1:]
                        if newword in friendsB:
                            return cnt
                        if newword != f and newword in wordList:
                            newfriends.add(newword)
                            wordList.remove(newword)
            if len(newfriends) < len(friendsB):
                friendsA, friendsB = newfriends, friendsB
            else:
                friendsB, friendsA = newfriends, friendsB
            cnt += 1
        return 0
