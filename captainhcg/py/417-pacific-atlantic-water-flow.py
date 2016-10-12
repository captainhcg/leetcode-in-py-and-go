class Solution(object):
    def pacificAtlantic(self, matrix):
        from collections import deque
        if not matrix or not(matrix[0]):
            return []

        rows, cols = len(matrix), len(matrix[0])
        pqueue, aqueue = deque(), deque()
        for y in xrange(rows):
            for x in xrange(cols):
                t = (y, x)
                if y == 0 or x == 0:
                    pqueue.append(t)
                if y == rows - 1 or x == cols - 1:
                    aqueue.append(t)

        def check(q):
            s = set()
            while q:
                y, x = q.popleft()
                if (y, x) in s:
                    continue
                s.add((y, x))
                for ny, nx in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
                    if ny < 0 or ny >= rows or nx < 0 or nx >= cols:
                        continue
                    if matrix[ny][nx] < matrix[y][x]:
                        continue
                    q.append((ny, nx))
            return s

        pset = check(pqueue)
        aset = check(aqueue)
        return sorted(list(p) for p in pset & aset)
