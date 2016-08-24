# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        dummy = TreeNode(0)
        
        def preOrder(prev, root):
            stack = [root]
            while stack:
                prev.right = stack[-1]
                node = stack.pop()
                prev = node
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    node.left = None
                    
        preOrder(dummy, root)
