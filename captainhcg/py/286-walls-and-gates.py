class Solution(object):
    def wallsAndGates(self, rooms):
        from collections import deque
        q = deque()

        for y in range(len(rooms)):
            for x in range(len(rooms[0])):
                if rooms[y][x] == 0:
                    q.append((y, x))

        def explore(y, x, v):
            process(y, x-1, v)
            process(y, x+1, v)
            process(y-1, x, v)
            process(y+1, x, v)

        def process(y, x, v):
            if y < 0 or y >= len(rooms) or x < 0 or x >= len(rooms[0]):
                return
            if rooms[y][x] < 0:
                return
            if rooms[y][x] <= v + 1:
                return
            rooms[y][x] = v + 1
            q.append((y, x))

        while q:
            y, x = q.popleft()
            v = rooms[y][x]
            explore(y, x, v)
