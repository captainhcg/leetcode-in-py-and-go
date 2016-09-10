class WordDictionary(object):
    def __init__(self):
        self.map = {}

    def addWord(self, word):
        chmap = self.map
        for ch in word:
            if ch not in chmap:
                chmap[ch] = {}
            chmap = chmap[ch]
        chmap["#"] = True

    def search(self, word):
        word += "#"
        def helper(w, startidx, chmap):
            for idx in xrange(startidx, len(w)):
                ch = w[idx]
                if ch == ".":
                    return any(helper(w, idx + 1, nextMap) for key, nextMap in chmap.iteritems() if key != "#")
                elif ch not in chmap:
                    return False
                elif ch == "#":
                    return True
                else:
                    chmap = chmap[ch]
                    
        return helper(word, 0, self.map)
