class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parents = {root: None}
        while stack:
            if p in parents and q in parents:
                break
            parent = stack.pop()
            if parent.left:
                parents[parent.left] = parent
                stack.append(parent.left)
            if parent.right:
                parents[parent.right] = parent
                stack.append(parent.right)
        pansestor = p
        pansestor_set = set()
        while pansestor:
            pansestor_set.add(pansestor)
            pansestor = parents[pansestor]
        
        qansestor = q
        while qansestor:
            if qansestor in pansestor_set:
                return qansestor
            else:
               qansestor = parents[qansestor]
