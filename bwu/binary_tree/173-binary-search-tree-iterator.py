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
        self._stack = []
        node = root
        while node:
            self._stack.append(node)
            node = node.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) > 0
            
    def next(self):
        """
        :rtype: int
        """
        ret = self._stack[-1]
        node = self._stack.pop()
        node = node.right
        while node:
            self._stack.append(node)
            node = node.left
        return ret.val
