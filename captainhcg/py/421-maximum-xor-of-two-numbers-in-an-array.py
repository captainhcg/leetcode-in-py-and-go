class Solution(object):
    def findMaximumXOR(self, nums):
        root = [None, None]
        _max = 0
        def insert(num):
            node = root
            for idx in xrange(30, -1, -1):
                n = (num >> idx) & 1
                if not node[n]:
                    node[n] = [None, None]
                node = node[n]
                
        def getMax(num):
            _sum = 0
            node = root
            for idx in xrange(30, -1, -1):
                n = (num >> idx) & 1
                looking_for = n ^ 1
                if node[looking_for]:
                    _sum += 1 << idx
                    node = node[looking_for]
                else:
                    node = node[n]
            return _sum
                
        for n in nums:
            insert(n)
            _max = max(getMax(n), _max)
        return _max
