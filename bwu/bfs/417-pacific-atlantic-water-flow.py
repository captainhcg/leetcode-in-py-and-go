class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        if not matrix or not matrix[0]:
            return ret
        pac, atl = [], []
        visited_pac, visited_atl = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            pac.append((i, 0))
            visited_pac.add((i, 0))
            atl.append((i, n - 1))
            visited_atl.add((i, n - 1))
        for j in xrange(n):
            pac.append((0, j))
            visited_pac.add((0, j))
            atl.append((m - 1, j))
            visited_atl.add((m - 1, j))
            
        self.bfs(pac, visited_pac, matrix, m, n)
        self.bfs(atl, visited_atl, matrix, m, n)
        
        for x, y in visited_pac & visited_atl:
            ret.append([x, y])
        return ret
        
    def bfs(self, queue, visited, matrix, m, n):
        while queue:
            c_x, c_y = queue.pop(0)
            for d_x, d_y in (0, 1), (0, -1), (1, 0), (-1, 0):
                n_x, n_y = c_x + d_x, c_y + d_y
                if 0 <= n_x < m and 0 <= n_y < n and (n_x, n_y) not in visited and matrix[n_x][n_y] >= matrix[c_x][c_y]:
                    queue.append((n_x, n_y))
                    visited.add((n_x, n_y))
