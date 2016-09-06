class Solution(object):
    def findMinHeightTrees(self, n, edges):
        from collections import defaultdict
        leaves = []
        remaining = set(xrange(n))
        if len(remaining) <= 2:
            return list(remaining)

        edges_set = defaultdict(set)
        for from_node, to_node in edges:
            edges_set[from_node].add(to_node)
            edges_set[to_node].add(from_node)

        for e in edges_set:
            if len(edges_set[e]) == 1:
                leaves.append(e)
                remaining.remove(e)

        while len(remaining) > 2:
            new_leaves = []
            for leaf_to_remove in leaves:
                for to_node in edges_set[leaf_to_remove]:
                    edges_set[to_node].remove(leaf_to_remove)
                    if len(edges_set[to_node]) == 1:
                        new_leaves.append(to_node)
                        remaining.remove(to_node)
            leaves = new_leaves

        return list(remaining)
