class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1:
            return True
            
        if not n or not edges:
            return False
            
        mapping = {i: set() for i in xrange(n)}
        for f, t in edges:
            mapping[f].add(t)
            mapping[t].add(f)
            
        node = set(i for i in xrange(n))
        queue = [edges[0][0]]
        while queue:
            curr = queue.pop(0)
            if curr not in node:
                return False
            node.remove(curr)
            if curr in mapping:
                for neighbor in mapping[curr]:
                    mapping[neighbor].remove(curr)
                    queue.append(neighbor)
            
        return not len(node)
                
