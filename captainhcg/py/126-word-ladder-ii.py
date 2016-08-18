class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        import string
        import collections
        if len(beginWord) != len(endWord):
            return []
        if beginWord == endWord:
            return [[beginWord]]
        friendsA, friendsB = set([beginWord]), set([endWord])
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        terminated = False
        pre_map = collections.defaultdict(list)
        ret = []

        def listAll(word):
            _ret = []
            def _dfs(arr, w):
                if w not in pre_map:
                    _ret.append(list(arr))
                    return
                for pre in pre_map[w]:
                    arr.append(pre)
                    _dfs(arr, pre)
                    arr.pop()
            _dfs([word], word)
            return _ret

        def combine_list(w1, w2):
            l1 = listAll(w1)
            l2 = listAll(w2)
            if l1[0][-1] != beginWord:
                l1, l2 = l2, l1
            for left in l1:
                for right in l2:
                    ret.append(left[::-1] + right)

        while friendsA and not terminated:
            newfriends = set([])
            for f in friendsA:
                for idx in xrange(len(f)):
                    for ch in string.ascii_lowercase:
                        newword = f[:idx] + ch + f[idx + 1:]
                        if newword == f:
                            continue
                        if newword in friendsB:
                            combine_list(f, newword)
                            terminated = True
                        elif newword in wordlist:
                            pre_map[newword].append(f)
                            newfriends.add(newword)
                            wordlist.remove(newword)
                        elif newword in newfriends:
                            pre_map[newword].append(f)
            if len(newfriends) < len(friendsB):
                friendsA, friendsB = newfriends, friendsB
            else:
                friendsB, friendsA = newfriends, friendsB
        return ret
