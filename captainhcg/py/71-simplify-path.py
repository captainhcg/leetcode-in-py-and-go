class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for e in path.split("/"):
            if not e or e == ".":
                continue
            elif e == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        return "/" + "/".join(stack)
