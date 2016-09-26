class Solution(object):
    def trapRainWater(self, heightMap):
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        import heapq
        
        visited = set()
        def make(row, col):
            visited.add((row, col))
            return (heightMap[row][col], row, col)
            
        heap = []
        for row in xrange(len(heightMap)):
            if row == 0 or row == len(heightMap) - 1:
                for col in xrange(len(heightMap[0])):
                    heapq.heappush(heap, make(row, col))
            else:
                heapq.heappush(heap, make(row, 0))
                heapq.heappush(heap, make(row, len(heightMap[0]) - 1))
        
        volume = 0
        while heap:
            h, y, x = heapq.heappop(heap)
            for newY, newX in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
                if (newY, newX) in visited or newY < 0 or newX < 0 or newY >= len(heightMap) or newX >= len(heightMap[0]):
                    continue
                visited.add((newY, newX))
                volume += max(0, h - heightMap[newY][newX])
                heapq.heappush(heap, (max(h, heightMap[newY][newX]), newY, newX))
        return volume
