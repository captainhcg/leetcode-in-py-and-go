class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        global_max = 0
        arr = [0] * len(matrix[0])
        
        def helper(arr):
            stack = [(0, -1)]
            _max = 0
            arr.append(0)
            for idx, h in enumerate(arr):
                while h < stack[-1][0]:
                    current_height, _ = stack.pop()
                    _max = max(_max, current_height * (idx - stack[-1][1] - 1))
                stack.append((h, idx))
            arr.pop()
            return _max
            
        for row in matrix:
            for idx, v in enumerate(row):
                if v == '1':
                    arr[idx] += 1
                else:
                    arr[idx] = 0
            global_max = max(global_max, helper(arr))
        return global_max
        
