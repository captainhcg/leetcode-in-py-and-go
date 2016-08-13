class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_h = right_h = 0
        lnd = rnd = root
        while lnd:
            left_h += 1
            lnd = lnd.left
        while rnd:
            right_h += 1
            rnd = rnd.right
        if left_h == right_h:
            return 2 ** left_h - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
        
