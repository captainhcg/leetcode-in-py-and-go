class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        ret = []
        for idx, n in enumerate(nums):
            while q and q[-1][1] < n:
                q.pop()
            q.append((idx, n))
            if idx >= k-1:
                while q[0][0] <= idx - k:
                    q.popleft()
                ret.append(q[0][1])
        return ret
