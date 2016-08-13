class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")
        stack = []
        def pop_pound():
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                del stack[-3:]
                stack.append("#")
            
        for ele in preorder:
            stack.append(ele)
            if ele == "#":
                pop_pound()
            
        return len(stack) == 1 and stack[0] == "#"
