class Solution(object):
    def getSkyline(self, buildings):
        import heapq
        valid_builds = []
        for idx, b in enumerate(buildings):
            valid_builds.append((b[0], -b[2], idx))
            valid_builds.append((b[1], b[2], idx))
        valid_builds.sort()
        heap = [(0, -1)]  # very important to put 0
        pre_height = 0
        removed = set()
        ret = []
        for x, h, key in valid_builds:
            if h < 0:
                heapq.heappush(heap, (h, key))
            else:
                removed.add(key)
            while heap[0][1] in removed:
                # the top tuple have been removed
                heapq.heappop(heap)
            top_height, _ = -heap[0]
            if top_height != pre_height:
                ret.append((x, top_height))
                pre_height = top_height
        return ret
