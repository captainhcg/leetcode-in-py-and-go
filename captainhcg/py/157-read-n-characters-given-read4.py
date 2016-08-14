class Solution(object):
    def read(self, buf, n):
        ch_read, remaining = 0, n
        read_buffer = [None] * 4
        while remaining > 0:
            new_read = read4(read_buffer)
            if new_read == 0:
                return ch_read
            for offset in xrange(min(new_read, remaining)):
                buf[ch_read] = read_buffer[offset]
                ch_read += 1
                remaining -= 1
        return ch_read
