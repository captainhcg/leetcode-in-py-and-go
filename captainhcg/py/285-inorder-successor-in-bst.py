class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        stack = []

        def helper(nd):
            while nd:
                stack.append(nd)
                nd = nd.left

        helper(root)
        last = None
        while stack:
            top = stack.pop()
            if last is p:
                return top
            last = top
            helper(top.right)

        return None
