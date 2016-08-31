class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            nd = TreeNode(head.val)
            nd.right = TreeNode(head.next.val)
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        ret = TreeNode(slow.next.val)
        ret.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        ret.left = self.sortedListToBST(head)
        return ret
