# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
            
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
            
        return root1.val == root2.val \
            and self.isMirror(root1.left, root2.right) \
            and self.isMirror(root1.right, root2.left)
