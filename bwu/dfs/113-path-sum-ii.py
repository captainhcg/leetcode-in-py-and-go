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
        ret = []
        if root is None:
            return ret
            
        self.dfs(root, sum, [], ret)
        return ret
        
        
    def dfs(self, root, target, tmp, ret):
        if root is None:
            return
        
        if root.left is None and root.right is None and target == root.val:
            ret.append(tmp + [root.val])
        else:
            self.dfs(root.left, target - root.val, tmp + [root.val], ret)
            self.dfs(root.right, target - root.val, tmp + [root.val], ret)
