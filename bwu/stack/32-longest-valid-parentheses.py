class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        stack = []
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        
        if not stack:
            return len(s)
            
        r = len(s)
        while stack:
            l = stack.pop()
            ret = max(ret, r - l - 1)
            r = l
            
        return max(ret, r)
