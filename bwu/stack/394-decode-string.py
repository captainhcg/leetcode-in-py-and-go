class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        res_stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ']':
                tmp = []
                while res_stack[-1] != '[':
                    tmp.append(res_stack.pop())
                res_stack.pop()
                res_stack += tmp[::-1] * num_stack.pop()
            elif c == '[':
                num_stack.append(num)
                res_stack.append(c)
                num = 0
            else:
                res_stack.append(c)
        return ''.join(res_stack)
