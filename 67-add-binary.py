class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        b = "0" * (len(a) - len(b)) + b
        ch_arr = []
        carry = 0
        for c1, c2 in zip(a[::-1], b[::-1]):
            s = int(c1) + int(c2) + carry
            if s >= 2:
                carry = 1
                s = s - 2
            else:
                carry = 0
            ch_arr.append(str(s))
        if carry:
            ch_arr.append(str(1))
        return "".join(ch_arr)[::-1]
