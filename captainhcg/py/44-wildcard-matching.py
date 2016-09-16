class Solution(object):
    def isMatch(self, s, p):
        if len(p.replace("*", "")) > len(s):
            return False
        prepended_s = "#" + s
        prepended_p = "#" + p
        last_arr = [False for _ in xrange(len(p) + 1)]
        last_arr[0] = True
        for j in xrange(1, len(p) + 1):
            last_arr[j] = last_arr[j-1] if prepended_p[j] == "*" else False
            
        for i in xrange(1, len(s) + 1):
            this_arr = [None] * (len(prepended_p))
            this_arr[0] = False
            for j in xrange(1, len(p) + 1):
                chp = prepended_p[j]
                if prepended_s[i] == chp or chp == "?":
                    this_arr[j] = last_arr[j-1]
                elif chp == "*":
                    this_arr[j] = last_arr[j-1] or this_arr[j-1] or last_arr[j]
                else:
                    this_arr[j] = False
            last_arr = this_arr
            
        return last_arr[-1]
