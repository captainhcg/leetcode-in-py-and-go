class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(m, n)
        cache = set()
        res = []
        for x, y in positions:
            uf.count += 1
            cache.add((x, y))
            if x - 1 >= 0 and (x - 1, y) in cache:
                uf.union((x, y), (x - 1, y))
            if x + 1 < m and (x + 1, y) in cache:
                uf.union((x, y), (x + 1, y))
            if y - 1 >= 0 and (x, y - 1) in cache:
                uf.union((x, y), (x, y - 1))
            if y + 1 < n and (x, y + 1) in cache:
                uf.union((x, y), (x, y + 1))
            res.append(uf.count)
            
        return res
        
class UnionFind(object):
    def __init__(self, m, n):
        self.father = {}
        for i in xrange(m):
            for j in xrange(n):
                self.father[(i, j)] = (i, j)
        self.count = 0
        
    def union(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        if find_a != find_b:
            self.father[find_a] = find_b
            self.count -= 1
        
    def find(self, i):
        if self.father[i] != i:
            self.father[i] = self.find(self.father[i])
        return self.father[i]
        
