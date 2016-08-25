# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
            
        preMid, mid = self.findMid(head)
        
        newHead = mid.next
        if preMid:
            preMid.next = None
            
        root = TreeNode(mid.val)
        if preMid:
            left = self.sortedListToBST(head)
            root.left = left
            
        right = self.sortedListToBST(newHead)
        root.right = right
        return root
        
        
    def findMid(self, head):
        if head is None:
            return None, head
            
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = head, head.next
        while fast and fast.next:
            dummy = slow
            slow = slow.next
            fast = fast.next.next
            
        if dummy.next == head:
            return None, slow
        
        return dummy, slow
