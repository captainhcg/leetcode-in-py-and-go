class Solution(object):
    def minCost(self, costs):
        l1, l2, l3 = 0, 0, 0
        for idx, (c1, c2, c3) in enumerate(costs):
            l1, l2, l3 = min(c1+l2, c1+l3), min(c2+l1, c2+l3), min(c3+l1, c3+l2)
        return min(l1, l2, l3)
