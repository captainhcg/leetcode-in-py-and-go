class Solution(object):
    def validUtf8(self, data):
        idx = 0
        while idx < len(data):
            ch = data[idx]
            if ch & (1 << 7) == 0:  # 1 byte
                idx += 1
            elif ch & (1 << 6):  # multiple bytes
                idx += 1
                len_bytes = 0
                if ch & (1 << 5) == 0:
                    len_bytes = 1
                elif ch & (1 << 4) == 0:
                    len_bytes = 2
                elif ch & (1 << 3) == 0:
                    len_bytes = 3
                else:
                    return False
                while len_bytes:
                    if idx >= len(data):
                        return False
                    ch = data[idx]
                    if ch & (1 << 7) and ch & (1 << 6) == 0:
                        len_bytes -= 1
                        idx += 1
                    else:
                        return False
            else:
                return False
        return True
