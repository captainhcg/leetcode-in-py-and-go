# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
            
        order = -1
        queue = [root]
        while queue:
            level = []
            order *= -1
            n = len(queue)
            for i in xrange(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
                
            if order > 0:
                ret.append(level)
            else:
                ret.append(level[::-1])
        return ret
