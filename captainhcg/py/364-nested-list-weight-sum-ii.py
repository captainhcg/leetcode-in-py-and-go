class Solution(object):
    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0
            
        def get_depth(ni):
            if ni.isInteger():
                return 1
            else:
                li = ni.getList()
                if li:
                    return max(get_depth(n) for n in li) + 1
            return 1
                
        def dfs(ni, level):
            if ni.isInteger():
                return level * ni.getInteger()
            else:
                return sum(dfs(n, level - 1) for n in ni.getList())
        
        level = max(get_depth(ni) for ni in nestedList)
        return sum(dfs(ni, level) for ni in nestedList)
