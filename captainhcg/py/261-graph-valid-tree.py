class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        from collections import deque
        if n < 2:
            return True
        
        edges_set = defaultdict(set)
        for from_node, to_node in edges:
            edges_set[from_node].add(to_node)
            edges_set[to_node].add(from_node)

        leaves = deque()
        visited = set()
        for e in edges_set:
            if len(edges_set[e]) <= 1:
                leaves.append(e)
                visited.add(e)
                break

        while leaves:
            leaf = leaves.popleft()
            for to_node in edges_set[leaf]:
                if to_node in visited:
                    return False
                visited.add(to_node)
                leaves.append(to_node)
                edges_set[to_node].remove(leaf)

        return len(visited) == n
