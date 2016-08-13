# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        self.inorder_dict = {}
        for idx, v in enumerate(inorder):
            self.inorder_dict[v] = idx
        return self.helper(0, len(preorder)-1, 0, len(inorder)-1)
    
    def helper(self, pst, ped, ist, ied):
        if pst > ped:
            return None
        pivot = self.preorder[pst]
        offset = self.inorder_dict[pivot] - ist
        nd = TreeNode(pivot)
        nd.left = self.helper(pst+1, pst+offset, ist, ist+offset-1)
        nd.right = self.helper(pst+1+offset, ped, ist+offset+1, ied)
        return nd
