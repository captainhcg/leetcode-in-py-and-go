class Solution(object):
    def findRadius(self, houses, heaters):
        import bisect
        heaters.sort()
        mindis = 0
        heaters.append(float("inf"))
        for h in houses:
            idx = bisect.bisect_left(heaters, h)
            if heaters[idx] == h:
                continue
            lidx, ridx = max(0, idx-1), idx
            ldis = abs(heaters[lidx] - h)
            rdis = abs(heaters[ridx] - h)
            mindis = max(mindis, min(ldis, rdis))
        return mindis
