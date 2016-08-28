# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        dummy = ListNode(0)
        newhead = ListNode(0)
        newhead.next = head
        dummy.next = head.next
        head.next = None
        cache = {'largest': head.val, 'last': head}
        
        def insert(node, nh):
            if node.val >= cache['largest']:
                cache['last'].next = node
                cache['largest'] = node.val
                cache['last'] = node
                node.next = None
                return
            
            curr = nh
            while curr.next and curr.next.val <= node.val:
                curr = curr.next
                
            if curr.next:
                node.next = curr.next
                curr.next = node
            else:
                curr.next = node
                node.next = None
                cache['largest'] = node.val
                cache['last'] = node
        
        while dummy.next:
            tmp = dummy.next.next
            insert(dummy.next, newhead)
            dummy.next = tmp
            
        return newhead.next
        
