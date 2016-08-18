class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                carry, res[i+j] = divmod(int(n2) * int(n1) + res[i+j], 10)
                res[i+j+1] += carry
        return "".join(str(i) for i in res[::-1]).lstrip("0") or "0"
