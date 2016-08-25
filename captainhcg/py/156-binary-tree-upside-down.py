class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root:
            return root
        ret_node = None
        nd = root
        while nd:
            ret_node = nd
            nd = nd.left

        def dfs(node):
            if node.left:
                dfs(node.left)
                node.left.left = node.right
                node.left.right = node
            node.left = node.right = None

        dfs(root)
        return ret_node
