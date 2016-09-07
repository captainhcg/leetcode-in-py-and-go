class Solution(object):
    def fullJustify(self, words, maxWidth):
        ret = []
        arr = []
        current_len = 0

        def add_line(last_line=False):
            if len(arr) == 1:
                line = arr[0]
            elif last_line:
                line = " ".join(arr)
            else:
                words_len = sum(len(w) for w in arr)
                spaces, padding = divmod(maxWidth - words_len, len(arr) - 1)
                line = "".rjust(spaces).join(["".rjust(spaces + 1).join(arr[:padding + 1]), "".rjust(spaces).join(arr[padding + 1:])])
            ret.append(line.ljust(maxWidth))

        for w in words:
            if current_len + len(arr) + len(w) > maxWidth:
                add_line(last_line=False)
                arr = []
                current_len = 0
            arr.append(w)
            current_len += len(w)
        add_line(last_line=True)

        return ret
