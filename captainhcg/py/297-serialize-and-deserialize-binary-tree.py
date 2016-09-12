from collections import deque

class Codec:
    
    def serialize(self, root):
        ret = []
        q = deque([(root, -1)])
        while q:
            node, parent = q.popleft()
            if not node:
                continue
            idx = len(ret)
            ret.append([node.val, -1, -1])
            if parent >= 0:
                ret[parent >> 1][1 + (parent & 1)] = idx
            q.append((node.left, idx << 1))
            q.append((node.right, (idx << 1) + 1))
        return ";".join([",".join(str(n) for n in nums) for nums in ret])

    def deserialize(self, data):
        if not data:
            return None
        arr = [node.split(",") for node in data.split(";")]
        def build(node_data):
            val, left_idx, right_idx = [int(v) for v in node_data]
            node = TreeNode(val)
            if left_idx >= 0:
                node.left = build(arr[left_idx])
            if right_idx >= 0:
                node.right = build(arr[right_idx])
            return node
        return build(arr[0])
