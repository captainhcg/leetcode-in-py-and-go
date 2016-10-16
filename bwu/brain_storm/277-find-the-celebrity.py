# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = [i for i in xrange(n)]
        while len(candidates) > 1:
            i = 0
            tmp = []
            while i + 1 < len(candidates):
                if knows(candidates[i], candidates[i + 1]):
                    tmp.append(candidates[i + 1])
                else:
                    tmp.append(candidates[i])
                i += 2
            if i == len(candidates) - 1:
                tmp.append(candidates[-1])
            candidates = tmp
            
        celeb = candidates[0]
        for i in xrange(n):
            if i == celeb:
                continue
            if not knows(i, celeb) or knows(celeb, i):
                return -1
        return celeb
