# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inddict = {val:i for i, val in enumerate(inorder)}
        
        if not inorder or not postorder:
            return None
            
        def helper(l, r):
            if l <= r:
                root = TreeNode(postorder.pop())
                idx = inddict[root.val]
                root.right = helper(idx + 1, r)
                root.left = helper(l, idx - 1)
                return root
        
        return helper(0, len(inorder) - 1)
