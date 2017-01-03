class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        adj = collections.defaultdict(set)
        for v, w in edges:
            adj[v].add(w)
            adj[w].add(v)
           
        queue = []
        unvisited = set(xrange(n))
        for i in xrange(n):
            if len(adj[i]) == 1:
                queue.append(i)
        
        while len(unvisited) > 2:
            length = len(queue)
            next_level = []
            for _ in xrange(length):
                curr = queue.pop(0)
                for nb in adj[curr]:
                    adj[nb].remove(curr)
                    if len(adj[nb]) == 1:
                        next_level.append(nb)
                unvisited.remove(curr)
            queue = next_level
        return list(unvisited)
