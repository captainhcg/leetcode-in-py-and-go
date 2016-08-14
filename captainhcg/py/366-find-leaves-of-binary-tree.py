class Solution(object):
    def findLeaves(self, root):
        ret = []
        def remove(nd):
            if not nd:
                return -1
            level = max(remove(nd.left), remove(nd.right)) + 1
            if len(ret) <= level:
                ret.append([])
            ret[level].append(nd.val)
            return level
    
        remove(root)
        return ret
