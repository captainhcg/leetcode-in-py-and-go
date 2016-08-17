class Solution(object):
    def minCostII(self, costs):
        if not costs or not costs[0]:
            return 0
        minamt, minidx, secamt = 0, -1, 0
        for house in costs:
            tmpmin, tmpidx, tmpsecmin = float("inf"), -1, float("inf")
            for color, cost in enumerate(house):
                total = minamt + cost if color != minidx else secamt + cost
                if total < tmpmin:
                    tmpsecmin = tmpmin
                    tmpmin = total
                    tmpidx = color
                elif total < tmpsecmin:
                    tmpsecmin = total
            minamt, minidx, secamt = tmpmin, tmpidx, tmpsecmin
        return tmpmin
