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
        if not n:
            return []
            
        def helper(l, r):
            if l >= r:
                return [None]
                
            ret = []
            for i in xrange(l, r):
                left = helper(l, i)
                right = helper(i + 1, r)
                for x in left:
                    for y in right:
                        root = TreeNode(i)
                        root.left = x
                        root.right = y
                        ret.append(root)
            return ret
                            
        return helper(1, n + 1)
