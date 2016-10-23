class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = float('-inf')
        def maxSum(root):
            if root is None:
                return 0
            l = maxSum(root.left)
            r = maxSum(root.right)
            self.sum = max(self.sum, root.val, root.val + l, root.val + r, root.val + l + r)
            return max(root.val, root.val + l, root.val + r)
            
        maxSum(root)
        return self.sum
