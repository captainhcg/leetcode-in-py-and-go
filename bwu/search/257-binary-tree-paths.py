# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret = []
        if root is None:
            return ret
        self.dfs(root, str(root.val), ret)
        return ret
        
    def dfs(self, root, tmp, res):
        if root.left is None and root.right is None:
            res.append(tmp)
        else:
            if root.left:
                self.dfs(root.left, tmp + '->' + str(root.left.val), res)
            if root.right:
                self.dfs(root.right, tmp + '->' + str(root.right.val), res)
