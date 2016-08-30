class Solution(object):
    def postorderTraversal(self, root):
        ret = []
        stack = [[root, 0]]

        while stack:
            ele, cnt = stack[-1]
            if not ele:
                stack.pop()
            elif cnt == 2:
                ret.append(ele.val)
                stack.pop()
            elif cnt == 1:
                stack[-1][1] += 1
                stack.append([ele.right, 0])
            else:  # cnt == 0
                stack[-1][1] += 1
                stack.append([ele.left, 0])
                
        return ret
