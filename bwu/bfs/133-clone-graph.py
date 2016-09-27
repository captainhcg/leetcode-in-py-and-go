# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
            
        mapping = {}
        queue = [node]
        visited = set([node])
        i = 0
        length = len(queue)
        
        while i < length:
            curr = queue[i]
            i += 1
            curr_clone = UndirectedGraphNode(curr.label)
            mapping[curr] = curr_clone
            for n in curr.neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
                    length += 1
                
        for n in queue:
            for neighbor in n.neighbors:
                mapping[n].neighbors.append(mapping[neighbor])
                
        return mapping[node]
