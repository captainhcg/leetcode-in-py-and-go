# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.tra(root, 0)
        return self.result[::-1]
    
    def tra(self, node, level):
        if not node:
            return
        if len(self.result) <= level:
            self.result.append([])
        self.result[level].append(node.val)
        self.tra(node.left, level+1)
        self.tra(node.right, level+1)
