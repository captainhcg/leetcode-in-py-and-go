class Solution(object):
    def shortestDistance(self, grid):
        from collections import deque
        if not grid or not grid[0]:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        distance_map = {}

        def bfs(row, col, level):
            visited = set((row, col))
            q = deque([(row + 1, col, 1), (row - 1, col, 1), (row, col + 1, 1), (row, col - 1, 1)])
            while q:
                y, x, steps = q.popleft()
                if y < 0 or y >= rows or x < 0 or x >= cols:
                    continue
                elif (y, x) in visited or grid[y][x] > 0:
                    continue
                visited.add((y, x))
                if (y, x) not in distance_map:
                    distance_map[(y, x)] = [0, 0]
                if distance_map[(y, x)][1] != level:
                    continue
                distance_map[(y, x)][0] += steps
                distance_map[(y, x)][1] += 1
                q.append((y + 1, x, steps + 1))
                q.append((y - 1, x, steps + 1))
                q.append((y, x + 1, steps + 1))
                q.append((y, x - 1, steps + 1))

        min_steps = float("inf")
        blds = 0
        level = 0
        for y in xrange(rows):
            for x in xrange(cols):
                if grid[y][x] == 1:
                    blds += 1
                    bfs(y, x, level)
                    level += 1

        for v in distance_map.itervalues():
            steps, _blds = v
            if _blds == blds:
                min_steps = min(min_steps, steps)

        if min_steps != float("inf"):
            return min_steps
        return -1
