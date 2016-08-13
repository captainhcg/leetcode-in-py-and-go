# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        nd = root
        while nd:
            self.stack.append(nd)
            nd = nd.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)
        

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        nd = top.right
        while nd:
            self.stack.append(nd)
            nd = nd.left
        return top.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
