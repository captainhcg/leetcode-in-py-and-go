# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.summ = 0
        
        self.dfs(root, 0)
        return self.summ
        
    def dfs(self, node, curr):
        curr = curr * 10 + node.val
        if not node.left and not node.right:
            self.summ += curr
            return
        if node.left:
            self.dfs(node.left, curr)
        if node.right:
            self.dfs(node.right, curr)
