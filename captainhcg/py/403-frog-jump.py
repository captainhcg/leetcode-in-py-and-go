class Solution(object):
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        sets = [set() for _ in xrange(len(stones))]
        sets[0].add(0)
        stones_map = dict((v, idx) for idx, v in enumerate(stones))
        for idx, stone in enumerate(stones):
            for k in sets[idx]:
                for d in (k-1, k, k+1):
                    if d <= 0: continue
                    if stone + d in stones_map:
                        sets[stones_map[stone + d]].add(d)
        return bool(sets[-1])
