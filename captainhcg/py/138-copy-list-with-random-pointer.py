class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        nodemap = {}
        node = head
        while node:
            for nd in (node, node.next, node.random):
                if nd and nd not in nodemap:
                    nodemap[nd] = RandomListNode(nd.label)
            node = node.next
        
        node = head
        while node:
            node_copy = nodemap[node]
            if node.next:
                node_copy.next = nodemap[node.next]
            if node.random:
                node_copy.random = nodemap[node.random]
            node = node.next
        
        return nodemap[head]
