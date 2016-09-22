class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        self.reverseHelper(s, 0, len(s) - 1)
        start, end = 0, 0
        while start < len(s):
            if s[start] == ' ':
                start += 1
                continue
            
            end = start
            while end < len(s) and s[end] != ' ':
                end += 1

            self.reverseHelper(s, start, end - 1)
            start = end + 1
        
        
    def reverseHelper(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return
        
