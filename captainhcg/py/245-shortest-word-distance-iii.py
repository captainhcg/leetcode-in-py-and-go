class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        idx1 = float("-inf")
        idx2 = float("inf")
        same = (word1 == word2)
        dis = float("inf")
        for idx, w in enumerate(words):
            cmpFlag = False
            if w == word1:
                cmpFlag = True
                idx1 = idx
            if w == word2:
                cmpFlag = True
                if same:
                    idx1 = idx2
                idx2 = idx
            if cmpFlag:
                dis = min(dis, abs(idx2 - idx1))
        return dis
