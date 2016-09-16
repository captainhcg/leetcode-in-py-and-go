class Solution(object):
    read_buffer = []
    legacy_buffer = []
    def read(self, buf, n):
        ch_read, ch_remaining = 0, n
        while self.legacy_buffer and ch_remaining:
            buf[ch_read] = self.legacy_buffer[0]
            self.legacy_buffer.pop(0)
            ch_read += 1
            ch_remaining -= 1
        if self.legacy_buffer:
            return ch_read

        while ch_remaining > 0:
            self.read_buffer = [None] * 4
            new_read = read4(self.read_buffer)
            if new_read == 0:
                break
            elif new_read > ch_remaining:
                self.legacy_buffer = [ch for ch in self.read_buffer[ch_remaining:] if ch is not None]
            for offset in xrange(min(new_read, ch_remaining)):
                buf[ch_read] = self.read_buffer[offset]
                ch_read += 1
                ch_remaining -= 1

        return ch_read
