class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1
            
        curr = root
        ret = float('inf')
        while curr:
            if abs(curr.val - target) < abs(ret - target):
                ret = curr.val
            if target == curr.val:
                return curr.val
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return ret
