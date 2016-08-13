class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return self.minDepth(root.left or root.right) + 1
