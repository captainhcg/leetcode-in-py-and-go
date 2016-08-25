class Solution(object):
    def longestConsecutive(self, root):
        self.max = 0
        self.dfs(root, None, 0)
        return self.max

    def dfs(self, nd, pval, pdeep):
        if not nd:
            return
        if pval is None or nd.val != pval + 1:
            deep = 1
        else:
            deep = pdeep + 1
        if deep > self.max:
            self.max = deep
        self.dfs(nd.left, nd.val, deep)
        self.dfs(nd.right, nd.val, deep)
