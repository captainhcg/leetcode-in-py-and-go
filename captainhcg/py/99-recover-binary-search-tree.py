class Solution(object):
    def recoverTree(self, root):
        pre = first = second = None
        stack = []

        def helper(node):
            while node:
                stack.append(node)
                node = node.left
        helper(root)

        while stack:
            current = stack.pop()
            if pre and current.val < pre.val:
                if not first:
                    first, second = pre, current
                else:
                    second = current
                    break
            pre = current
            helper(current.right)

        first.val, second.val = second.val, first.val
        return
