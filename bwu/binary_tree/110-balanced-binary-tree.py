# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depthAndBal(root)[1]
        
    def depthAndBal(self, root):
        if root is None:
            return (0, True)
            
        l_d, l_b = self.depthAndBal(root.left)
        r_d, r_b = self.depthAndBal(root.right)
        
        depth = max(l_d, r_d) + 1
        if l_b and r_b and abs(l_d - r_d) <= 1:
            return (depth, True)
        else:
            return (depth, False)
