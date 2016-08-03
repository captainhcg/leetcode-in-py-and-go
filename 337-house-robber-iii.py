# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.rob_helper(root))
    
    def rob_helper(self, nd):
        if not nd:
            return 0, 0
        lc, lfc = self.rob_helper(nd.left)
        rc, rfc = self.rob_helper(nd.right)
        max_next_level = lc + rc
        max_this_level = max(nd.val + lfc + rfc, max_next_level)
        return max_this_level, max_next_level
