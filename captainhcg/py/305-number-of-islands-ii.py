class Solution(object):
    def numIslands2(self, m, n, positions):
        self.islands_set = {}
        self.islands_tree = {}
        self.grid = [[0] * n for _ in xrange(m)]

        def merge_sets(fromy, fromx, toy, tox):
            if toy < 0 or toy >= m or tox < 0 or tox >= n or self.grid[toy][tox] != 1:
                return
            merge_from_parent = self.islands_tree[fromy, fromx]
            merge_to_parent = self.islands_tree[toy, tox]
            if merge_from_parent == merge_to_parent:
                return
            elif len(self.islands_set[merge_from_parent]) >  len(self.islands_set[merge_to_parent]):
                merge_to_parent, merge_from_parent = merge_from_parent, merge_to_parent
            for node in self.islands_set[merge_from_parent]:
                self.islands_set[merge_to_parent].add(node)
                self.islands_tree[node] = merge_to_parent
            del self.islands_set[merge_from_parent]

        ret = []
        for y, x in positions:
            self.grid[y][x] = 1
            self.islands_set[(y, x)] = set([(y, x)])
            self.islands_tree[(y, x)] = (y, x)
            merge_sets(y, x, y-1, x)
            merge_sets(y, x, y+1, x)
            merge_sets(y, x, y, x-1)
            merge_sets(y, x, y, x+1)
            ret.append(len(self.islands_set))
            
        return ret
