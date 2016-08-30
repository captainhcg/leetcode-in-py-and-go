class Solution(object):
    def longestValidParentheses(self, s):
        mlen = 0
        lastleft = -1
        stack = []
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            else:
                if not stack:
                    lastleft = idx
                else:
                    stack.pop()
                    if stack:
                        mlen = max(mlen, idx - stack[-1])
                    else:
                        mlen = max(mlen, idx - lastleft)
        return mlen
