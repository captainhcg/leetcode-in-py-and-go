class Solution(object):
    def kthSmallest(self, matrix, k):
        import heapq
        minheap = []
        for idx, n in enumerate(matrix[0]):
            heapq.heappush(minheap, (n, idx, 0))
        cnt = 0
        while minheap:
            cnt += 1
            val, col, row = heapq.heappop(minheap)
            if cnt == k:
                return val
            if row + 1 < len(matrix):
                heapq.heappush(minheap, (matrix[row+1][col], col, row+1))
