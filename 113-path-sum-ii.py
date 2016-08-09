# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper([], root, sum)
        return self.ret
    
    def helper(self, arr, nd, target):
        if not nd:
            return
        target = target - nd.val
        arr.append(nd.val)
        if not nd.left and not nd.right:
            if target == 0:
                self.ret.append(list(arr))
        self.helper(arr, nd.left, target)
        self.helper(arr, nd.right, target)
        arr.pop()
