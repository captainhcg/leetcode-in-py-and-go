class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [(0, -1)]
        maxarea = 0
        heights.append(0)
        for idx, h in enumerate(heights):
            while h < stack[-1][0]:
                current_height, _ = stack.pop()
                left_idx, right_idx = stack[-1][1], idx
                maxarea = max(maxarea, (right_idx - left_idx - 1) * current_height)
            stack.append((h, idx))
        return maxarea
