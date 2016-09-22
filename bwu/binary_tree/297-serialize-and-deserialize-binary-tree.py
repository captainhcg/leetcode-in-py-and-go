# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            for i in xrange(length):
                node = queue.pop(0)
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('#')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        idx = 1
        root = TreeNode(int(nodes[0]))
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if nodes[idx] != '#':
                curr.left = TreeNode(int(nodes[idx]))
                queue.append(curr.left)
            idx += 1
            if nodes[idx] != '#':
                curr.right = TreeNode(int(nodes[idx])) 
                queue.append(curr.right)
            idx += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
