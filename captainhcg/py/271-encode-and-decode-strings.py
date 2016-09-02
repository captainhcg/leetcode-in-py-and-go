class Codec:

    def encode(self, strs):
        return "".join((",".join(str(len(s)) for s in strs), "#", "".join(strs)))

    def decode(self, s):
        header, s = s.split("#", 1)
        headers = header.split(",") if header else []
        ret = []
        offset = 0
        for slen in headers:
            ret.append(s[offset:offset + int(slen)])
            offset += int(slen)
        return ret
