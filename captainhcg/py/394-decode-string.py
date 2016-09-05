class Solution(object):
    def decodeString(self, s):
        nstack = []
        cstack = [""]
        for idx, ch in enumerate(s):
            if ch.isdigit():
                if idx and s[idx-1].isdigit():
                    nstack[-1] = nstack[-1] * 10 + int(ch)
                else:
                    nstack.append(int(ch))
            elif ch == "[":
                cstack.append("")
            elif ch == "]":
                tmp_str = cstack.pop() * nstack.pop()
                cstack[-1] += tmp_str
            else:
                cstack[-1] += ch
        return cstack[-1]
