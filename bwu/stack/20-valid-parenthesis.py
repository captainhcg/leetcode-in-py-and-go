class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right, stack = '({[', ')}]', []
        mapping = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not len(stack):
                    return False
                if stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
