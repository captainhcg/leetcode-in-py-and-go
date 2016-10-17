class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return 0
            
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val
            
        sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return sum
