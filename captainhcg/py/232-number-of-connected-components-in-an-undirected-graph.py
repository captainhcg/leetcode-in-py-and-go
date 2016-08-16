class Solution(object):
    def countComponents(self, n, edges):
        parents = range(n)
        def findParent(nd):
            if parents[nd] != nd:
                parents[nd] = findParent(parents[nd])
            return parents[nd]
        
        for s, e in edges:
            parents[findParent(s)] = findParent(parents[e])

        return len(set(findParent(idx) for idx in xrange(n)))
