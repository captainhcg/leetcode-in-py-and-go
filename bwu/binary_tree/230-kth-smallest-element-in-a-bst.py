# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if k == 1:
                    return node.val
                k -= 1
                node = node.right
                
        return
