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

    def sumOfLeftLeaves2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res
            
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if node.right.left or node.right.right:
                    stack.append(node.right)
                    
        return res
