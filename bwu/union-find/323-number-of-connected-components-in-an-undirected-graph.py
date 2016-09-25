class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for f, t in edges:
            uf.union(f, t)
            
        return uf.count
        
class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.root = [0] * n
        self.rank = [0] * n
        for i in xrange(n):
            self.root[i] = i
            
    def union(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        
        if find_a != find_b:
            if self.rank[find_a] < self.rank[find_b]:
                self.root[find_a] = find_b
            elif self.rank[find_b] < self.rank[find_a]:
                self.root[find_b] = find_a
            else:
                self.root[find_a] = find_b
                self.rank[find_a] += 1

            self.count -= 1
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
            
        return self.root[a]
