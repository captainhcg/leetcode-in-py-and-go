class Solution(object):
    def lengthLongestPath(self, input):
        eles = input.split("\n")

        def get_level(s):
            oldlen = len(s)
            s = s.lstrip("\t")
            return oldlen - len(s), s

        maxlen = 0
        stack = []
        for e in eles:
            level, s = get_level(e)
            if len(stack) <= level:
                stack.append(0)
            stack[level] = len(s)
            if level > 0:
                stack[level] += stack[level-1]
            if "." in s:
                maxlen = max(maxlen, stack[level] + level)
        return maxlen
