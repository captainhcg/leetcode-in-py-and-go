class Solution(object):
    size = 0
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.size
        
    def helper(self, root):
        if root is None:
            return
        if root.left and root.right:
            ls, ll, lh = self.helper(root.left)
            rs, rl, rh = self.helper(root.right)
            if ls > 0 and rs > 0 and lh < root.val < rl:
                self.size = max(self.size, ls + rs + 1)
                return (ls + rs + 1, ll, rh)
            else:
                return (-1, 0, 0)
        elif root.left:
            ls, ll, lh = self.helper(root.left)
            if ls > 0 and lh < root.val:
                self.size = max(self.size, ls + 1)
                return (ls + 1, ll, root.val)
            else:
                return (-1, 0, 0)
        elif root.right:
            rs, rl, rh = self.helper(root.right)
            if rs > 0 and root.val < rl:
                self.size = max(self.size, rs + 1)
                return (rs + 1, root.val, rh)
            else:
                return (-1, 0, 0)
        else:
            self.size = max(self.size, 1)
            return (1, root.val, root.val)
