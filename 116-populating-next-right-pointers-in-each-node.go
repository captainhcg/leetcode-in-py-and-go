# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return root
        next_head = root
        while next_head and next_head.left:
            pre = None
            cur = next_head
            next_head = cur.left
            while cur:
                if pre:
                    pre.next = cur.left
                cur.left.next = cur.right
                pre = cur.right
                cur = cur.next
