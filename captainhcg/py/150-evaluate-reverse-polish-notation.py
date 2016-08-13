import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numstack =[]
        for token in tokens:
            if token in "+-*/":
                n2, n1 = numstack.pop(), numstack.pop()
                if token == "+":
                    v = n1 + n2
                elif token == "-":
                    v = n1 - n2
                elif token == "*":
                    v = n1 * n2
                elif token == "/":
                    v = int(operator.truediv(n1, n2))
                numstack.append(v)
            else:
                numstack.append(int(token))
        return numstack.pop()
