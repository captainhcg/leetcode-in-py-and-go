class Solution(object):
    def findLadders(self, start, end, dict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        ret = []
        prevMap = {}
        length = len(start)
        candidates, current, previous = [set(), set()], 0, 1
        
        for word in dict:
                prevMap[word] = []
                
        candidates[current].add(start)
        
        while True:
            current, previous = previous, current
            for word in candidates[previous]:
                dict.remove(word)
                
            candidates[current].clear()
            
            for word in candidates[previous]:
                for i in range(length):
                    for c in string.lowercase:
                        if word[i] != c:
                            newWord = word[:i] + c + word[i + 1:]
                            if newWord in dict:
                                candidates[current].add(newWord)
                                prevMap[newWord].append(word)
                                
            if len(candidates[current]) == 0:
                return ret
            if end in candidates[current]:
                break
            
        self.buildPath([end], start, end, prevMap, ret)
        return ret
        
    def buildPath(self, path, start, word, prevMap, ret):
        if word == start:
            ret.append(path[::-1])
            return
        
        for i in prevMap[word]:
            self.buildPath(path + [i], start, i, prevMap, ret)               
        
