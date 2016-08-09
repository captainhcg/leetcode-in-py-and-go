# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper([], root)
        return self.ret
    
    def helper(self, arr, nd):
        if not nd:
            return
    
        arr.append(str(nd.val))
        if not nd.left and not nd.right:
            self.ret += int("".join(arr))
        self.helper(arr, nd.left)
        self.helper(arr, nd.right)
        arr.pop()
        
        
