class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = []
        curr = root
        prev = None
        pivot = None
        swap = None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if pivot:
                    if swap.val > curr.val:
                        swap = curr
                elif prev and curr.val < prev.val:
                    pivot = prev
                    swap = curr
                prev = curr
                curr = curr.right
        pivot.val, swap.val = swap.val, pivot.val
        return
