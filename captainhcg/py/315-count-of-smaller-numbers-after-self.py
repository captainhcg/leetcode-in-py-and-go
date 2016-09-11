class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0
        self.smaller = 0

class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []

        root = Node(float("inf"))
        ret = []

        def insert(node, v, cnt):
            if v == node.val:
                ret.append(cnt + node.smaller)
                node.count += 1
            elif v < node.val:
                node.smaller += 1
                if not node.left:
                    node.left = Node(v)
                insert(node.left, v, cnt)
            elif v > node.val:
                cnt += node.smaller + node.count
                if not node.right:
                    node.right = Node(v)
                insert(node.right, v, cnt)

        for n in nums[::-1]:
            insert(root, n, 0)

        return ret[::-1]
