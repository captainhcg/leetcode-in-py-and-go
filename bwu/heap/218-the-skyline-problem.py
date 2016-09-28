class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        points = []
        for idx, b in enumerate(buildings):
            points.append((b[0], -b[2], idx))
            points.append((b[1], b[2], idx))
            
        points.sort()
        heap = [(0, -1)]
        res = []
        removed = set()
        pre_top = 0
        
        for x, h, key in points:
            if h < 0:
                heapq.heappush(heap, (h, key))
            else:
                removed.add(key)
            
            while heap[0][1] in removed:
                heapq.heappop(heap)
                
            top = -heap[0][0]
            if top != pre_top:
                res.append((x, top))
                pre_top = top

        return res
