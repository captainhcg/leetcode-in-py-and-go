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
        self.ret = []
        self.helper(root, [])
        return self.ret
    
    def helper(self, node, parents):
        if not node:
            return
        parents.append(str(node.val))
        if not node.left and not node.right:
            self.ret.append("->".join(parents))
        self.helper(node.left, parents)
        self.helper(node.right, parents)
        parents.pop()
