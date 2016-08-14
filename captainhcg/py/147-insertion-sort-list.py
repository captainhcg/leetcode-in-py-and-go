class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        node = last = head
        largest = float('inf')
        info = {'largest': float('inf'), 'last': None}
        
        def insert(node):
            if node.val > info['largest']:
                info['last'].next = node
                info['last'] = node
                info['largest'] = node.val
                return
            pre = dummy
            cur = dummy.next
            while cur:
                if node.val <= cur.val:
                    pre.next = node
                    node.next = cur
                    return
                else:
                    pre = cur
                    cur = cur.next
            pre.next = node
            info['last'] = node
            info['largest'] = node.val
            
        while node:
            node_next = node.next
            node.next = None
            insert(node)
            node = node_next
        
        return dummy.next
