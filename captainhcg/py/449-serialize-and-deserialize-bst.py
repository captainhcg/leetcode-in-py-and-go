class Codec:

    def serialize(self, root):
        ret = []
        def dfs(node):
            if not node:
                ret.append("#")
            else:
                ret.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(ret)
        

    def deserialize(self, data):
        it = iter(data.split(","))
        def getNode():
            v = next(it)
            if v == "#":
                return None
            nd = TreeNode(int(v))
            nd.left = getNode()
            nd.right = getNode()
            return nd
        root = getNode()
        
        return root
