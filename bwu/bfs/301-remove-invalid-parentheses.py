class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = set()
        found = False
        queue = [s]
        visited = set()
        while queue:
            length = len(queue)
            for i in xrange(length):
                curr = queue.pop(0)
                if self.isValid(curr):
                    return [curr]
                    
                for j in xrange(len(curr)):
                    if curr[j] not in '()':
                        continue
                    tmp = curr[:j] + curr[j + 1:]
                    if tmp in visited:
                        continue
                    visited.add(tmp)
                    if not self.isValid(tmp):
                        queue.append(tmp)
                    else:
                        found = True
                        ret.add(tmp)
                        
            if found:
                return list(ret)
        return [s]
                
        
    def isValid(self, s):
        count = 0
        idx = 0
        for n in s:
            if n == '(':
                count += 1
            elif n == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0
