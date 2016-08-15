class Solution(object):
    def maxPathSum(self, root):
        self.max = root.val
        self.dfs(root)
        return self.max
        
    def dfs(self, node):
        if not node:
            return float('-inf')
        lm = self.dfs(node.left)
        rm = self.dfs(node.right)
        self.max = max(self.max, node.val, lm + node.val, rm + node.val, rm + lm + node.val)
        return max(node.val, node.val + lm, node.val + rm)
