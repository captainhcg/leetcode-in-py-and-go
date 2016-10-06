class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for d in dirs:
            if not d or d == '.':
                continue
            elif d == '..':
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(d)
                
        return '/' + '/'.join(stack)
