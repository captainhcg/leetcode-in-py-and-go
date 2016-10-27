class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign, stack, res = 0, 1, [], 0
        for n in s + '+':
            if n.isdigit():
                num = num * 10 + int(n)
            elif n in '+-':
                res += num * sign
                num = 0
                sign = 1 if n == '+' else -1
            elif n == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif n == ')':
                res += num * sign
                num = res
                sign = stack.pop()
                res = stack.pop()
        return res
