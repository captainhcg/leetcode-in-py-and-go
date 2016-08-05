# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ret = []
        self.tra(root, 0)
        return self.ret
    
    def tra(self, node, level):
        if not node:
            return
        if len(self.ret) <= level:
            self.ret.append([])
        self.ret[level].append(node.val)
        self.tra(node.left, level+1)
        self.tra(node.right, level+1)
