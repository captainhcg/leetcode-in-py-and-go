# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]
        
    def helper(self, root):
        if not root:
            return (True, float('-inf'), float('inf'))
        
        if root.left and root.right:
            validL, minL, maxL = self.helper(root.left)
            validR, minR, maxR = self.helper(root.right)
            return (validL and validR and maxL < root.val < minR, minL, maxR)
        elif root.left:
            validL, minL, maxL = self.helper(root.left)
            return (validL and maxL < root.val, minL, root.val)
        elif root.right:
            validR, minR, maxR = self.helper(root.right)
            return (validR and root.val < minR, root.val, maxR)
        else:
            return (True, root.val, root.val)
