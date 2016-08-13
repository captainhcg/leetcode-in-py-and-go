class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        self.ret = []
        self.helper([], n, k)
        return self.ret
    
    def helper(self, arr, n, k):
        if k == 0:
            self.ret.append(list(arr))
            return
        if n < k:
            return
        arr.append(n)
        self.helper(arr, n-1, k-1)
        arr.pop()
        self.helper(arr, n-1, k)
