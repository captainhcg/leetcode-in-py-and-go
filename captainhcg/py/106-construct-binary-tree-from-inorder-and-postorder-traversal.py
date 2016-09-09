class Solution(object):
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        return self.bt(0, len(inorder) - 1, 0, len(postorder) - 1)

    def bt(self, istart, iend, pstart, pend):
        if istart > iend:
            return None
        node = TreeNode(self.postorder[pend])
        offset = 0
        for idx in xrange(istart, iend + 1):
            if self.inorder[idx] == node.val:
                break
            offset += 1
        node.left = self.bt(istart, istart + offset - 1, pstart, pstart + offset - 1)
        node.right = self.bt(istart + offset + 1, iend, pstart + offset, pend - 1)
        return node
