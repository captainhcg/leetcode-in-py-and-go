# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if not n:
            return None
            
        mid = nums[n / 2]
        node = TreeNode(mid)
        left = self.sortedArrayToBST(nums[: n / 2])
        right = self.sortedArrayToBST(nums[(n / 2) + 1:])
        node.left = left
        node.right = right
        
        return node
