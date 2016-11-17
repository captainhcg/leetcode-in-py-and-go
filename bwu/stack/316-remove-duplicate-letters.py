class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        counts = {}
        visited = set()
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
                
        for c in s:
            counts[c] -= 1
            if c in visited:
                continue
            while stack and stack[-1] > c and counts[stack[-1]] > 0:
                visited.discard(stack[-1])
                stack.pop()
            visited.add(c)
            stack.append(c)
            
        return ''.join(stack)
