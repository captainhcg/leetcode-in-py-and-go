class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
            
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        
        return root
