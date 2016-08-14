class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(nlist, level):
            s = 0
            for n in nlist:
                if n.isInteger():
                    s += level * n.getInteger()
                else:
                    s += helper(n.getList(), level+1)
            return s
        
        return helper(nestedList, 1)
