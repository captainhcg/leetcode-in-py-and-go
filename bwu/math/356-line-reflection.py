import collections
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        minx, maxx = float('inf'), float('-inf')
        visited = collections.defaultdict(set)
        for p in points:
            minx = min(minx, p[0])
            maxx = max(maxx, p[0])
            visited[p[1]].add(p[0])
        midx = minx + maxx
        for p in points:
            if midx - p[0] not in visited[p[1]]:
                return False
        return True
