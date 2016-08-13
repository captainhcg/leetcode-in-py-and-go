class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        nmap = dict()
        stack = [node]
        while stack:
            nd = stack.pop()
            nmap[nd] = UndirectedGraphNode(nd.label)
            [stack.append(ch) for ch in nd.neighbors if ch not in nmap]
        
        for original_node, new_node in nmap.iteritems():
            [new_node.neighbors.append(nmap[bd]) for bd in original_node.neighbors]
        
        return nmap[node]
