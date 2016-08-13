# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.helper(1, n)
    
    def helper(self, st, ed):
        if st > ed:
            return [None]
        ret = []
        for v in xrange(st, ed+1):
            left = self.helper(st, v-1)
            right = self.helper(v+1, ed)
            for lnd in left:
                for rnd in right:
                    r = TreeNode(v)
                    r.left = lnd
                    r.right = rnd
                    ret.append(r)
        return ret
