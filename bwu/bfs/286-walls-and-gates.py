class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        queue = []
        visited = set()
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
            
        while queue:
            length = len(queue)
            for i in xrange(length):
                curr_x, curr_y = queue.pop(0)
                
                for d_x, d_y in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if (0 <= curr_x + d_x < len(rooms) and 0 <= curr_y + d_y < len(rooms[0]) and (curr_x + d_x, curr_y + d_y) not in visited and rooms[curr_x + d_x][curr_y + d_y] > 2 ** 30):
                        queue.append((curr_x + d_x, curr_y + d_y))
                        visited.add((curr_x + d_x, curr_y + d_y))
                        rooms[curr_x + d_x][curr_y + d_y] = rooms[curr_x][curr_y] + 1
        return
