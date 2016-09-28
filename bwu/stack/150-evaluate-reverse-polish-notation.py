import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if x in '+-*/':
                if len(stack) < 2:
                    return -1
                op2 = stack.pop()
                op1 = stack.pop()
                if x == '+':
                    tmp = op1 + op2
                elif x == '-':
                    tmp = op1 - op2
                elif x == '*':
                    tmp = op1 * op2
                elif op2 == 0:
                    return -1
                else:
                    tmp = int(operator.truediv(op1, op2))
                stack.append(tmp)
            else:
                stack.append(int(x))
        
        if len(stack) != 1:
            return -1
        else:
            return stack[0]
