class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        uf = UnionFind(m, n)
        cache = set()
        for i in xrange(m):
            for j in xrange(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    uf.union((i, j), (m, n))
                    cache.add((i, j))
                elif board[i][j] == 'O':
                    cache.add((i, j))
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        if board[i + dx][j + dy] == 'O':
                            cache.add((i + dx, j + dy))
                            uf.union((i, j), (i + dx, j + dy))
                        
        for i, j in cache:          
            if board[i][j] == 'O' and not uf.connected((i, j), (m, n)):
                board[i][j] = 'X'
                
        return
        
class UnionFind(object):
    def __init__(self, m, n):
        self.count = 0
        self.root = {}
        for i in xrange(m):
            for j in xrange(n):
                self.root[(i, j)] = (i, j)
        self.root[(m, n)] = (m, n)
                
        
    def union(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        
        if find_a != find_b:
            self.root[find_a] = find_b
            self.count -= 1
            
    def connected(self, a, b):
        return self.find(a) == self.find(b)
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
            
        return self.root[a]
    
