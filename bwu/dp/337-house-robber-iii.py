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
        def dfs(root):
            if not root:
                return (0, 0)
            left, left_n = dfs(root.left)
            right, right_n = dfs(root.right)
            nl = left + right
            l = max(root.val + left_n + right_n, nl)
            return l, nl
            
        return dfs(root)[0]
