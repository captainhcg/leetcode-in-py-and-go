class Solution(object):
    def parseTernary(self, expression):
        tokens = []
        last_ch = ""
        for ch in expression:
            if ch.isdigit() and last_ch.isdigit():
                tokens[-1] += ch
            elif ch != ":":
                tokens.append(ch)
            last_ch = ch

        values = []
        while tokens:
            v = tokens.pop()
            if v == "?":
                bool_value = tokens.pop()
                tvalue, fvalue = values.pop(), values.pop()
                if bool_value == "T":
                    values.append(tvalue)
                else:
                    values.append(fvalue)
            else:
                values.append(v)

        return values[0]
