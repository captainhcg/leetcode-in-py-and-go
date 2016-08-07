class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper([], k, n, 9)
        return [list(r) for r in self.ret]


    def helper(self, arr, k, n, up_to):
        if n <= 0 or up_to <= 0 or k <= 0:
            return
        if k == 1 and up_to == n:
            self.ret.append(tuple(arr) + (up_to,))
            return
        arr.append(up_to)
        self.helper(arr, k-1, n-up_to, up_to-1)
        arr.pop()
        self.helper(arr, k, n, up_to-1)
