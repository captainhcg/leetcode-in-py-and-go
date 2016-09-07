from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        self.listMap = defaultdict(list)
        for idx, word in enumerate(words):
            self.listMap[word].append(idx)

    def shortest(self, word1, word2):
        l1, l2 = self.listMap[word1], self.listMap[word2]
        s1 = s2 = 0
        dis = float("inf")
        while s1 < len(l1) and s2 < len(l2):
            dis = min(dis, abs(l1[s1] - l2[s2]))
            if l1[s1] < l2[s2]:
                s1 += 1
            else:
                s2 += 1
        return dis
