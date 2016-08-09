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
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, nd, minn, maxn):
        if not nd:
            return True
        if not minn < nd.val < maxn:
            return False
        return self.helper(nd.left, minn, nd.val) and self.helper(nd.right, nd.val, maxn)
