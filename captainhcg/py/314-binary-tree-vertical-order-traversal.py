class Solution(object):
    def verticalOrder(self, root):
        from collections import defaultdict
        from collections import deque
        m = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if not node:
                continue
            m[level].append(node.val)
            q.append((node.left, level-1))
            q.append((node.right, level+1))
        ret = []
        for level in sorted(m.keys()):
            ret.append(m[level])
        return ret
