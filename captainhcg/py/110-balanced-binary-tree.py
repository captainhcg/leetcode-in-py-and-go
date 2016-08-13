# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isBal, _ = self.balHelper(root)
        return isBal
        
    def balHelper(self, node):
        if not node:
            return True, 0
        leftBal, leftDep = self.balHelper(node.left)
        rightBal, rightDep = self.balHelper(node.right)
        maxDep = max(leftDep, rightDep)
        isBal = (abs(leftDep - rightDep) <= 1)
        return (isBal and rightBal and leftBal), maxDep + 1
