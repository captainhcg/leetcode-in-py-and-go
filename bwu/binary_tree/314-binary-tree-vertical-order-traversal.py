class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        queue = [(root,0)]
        levels = []
        while queue:
            level = []
            length = len(queue)
            for i in xrange(length):
                curr, curr_p = queue.pop(0)
                level.append((curr.val, curr_p))
                if curr.left:
                    queue.append((curr.left, curr_p - 1))
                if curr.right:
                    queue.append((curr.right, curr_p + 1))
            levels.append(level)
            
        ret = []
        mapping = collections.defaultdict(list)
        for level in levels:
            for c, c_p in level:
                mapping[c_p].append(c)
                
        for k in sorted(mapping.keys()):
            ret.append(mapping[k])
        return ret
