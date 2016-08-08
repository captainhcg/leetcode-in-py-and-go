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
        self.ret = []
        self.helper(root, 0)
        for idx in xrange(len(self.ret)):
            if idx % 2 == 1:
                self.ret[idx] = self.ret[idx][::-1]
        return self.ret
        
    def helper(self, nd, level):
        if not nd:
            return
        if len(self.ret) <= level:
            self.ret.append([])
        self.ret[level].append(nd.val)
        self.helper(nd.left, level+1)
        self.helper(nd.right, level+1)
