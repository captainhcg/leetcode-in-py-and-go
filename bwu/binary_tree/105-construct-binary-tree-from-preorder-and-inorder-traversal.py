# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        idxmap = {val:idx for idx, val in enumerate(inorder)}
        
        if not preorder or not inorder:
            return None
            
        def helper(l, r):
            if l <= r:
                root = TreeNode(preorder.pop(0))
                idx = idxmap[root.val]
                root.left = helper(l, idx - 1)
                root.right = helper(idx + 1, r)
                return root
                
        return helper(0, len(inorder) - 1)
        
