class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        arr = self.preprocess(points)
        if len(arr) == 1:
            return arr[0][2]
        global_max =0
        for idx, p1 in enumerate(arr):
            cnt_map = {}
            for jdx, p2 in enumerate(arr[idx+1:]):
                key = self.make_key(p1[0], p1[1], p2[0], p2[1])
                cnt_map[key] = cnt_map.get(key, p1[2]) + p2[2]
                global_max = max(global_max, cnt_map[key])
        return global_max
    
    def make_key(self, x1, y1, x2, y2):
        if x1 == x2:
            return (x1, 0, 0, 0)
        if y1 == y2:
            return (0, y1, 0, 0)
        a = float(y1-y2)/(x1-x2)
        b = float(y1 + y2) - float((y1-y2) * (x1 + x2)/(x1-x2))
        return (0, 0, a, b)
        
    def preprocess(self, points):
        m = {}
        for p in points:
            m[(p.x, p.y)] = m.get((p.x, p.y), 0) + 1
        arr = [(k[0], k[1], v) for k, v in m.iteritems()]
        arr.sort()
        return arr
