class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for ch in num:
            if not stack or ch >= stack[-1]:
                pass
            else:
                while k and stack and stack[-1] > ch:
                    stack.pop()
                    k -= 1
            stack.append(ch)
        while k and stack:
            stack.pop()
            k -= 1
        return str("".join(stack)).lstrip("0") or "0"
