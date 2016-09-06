class Solution(object):
    def removeInvalidParentheses(self, s):
        from collections import deque
        queue = deque([s])
        visited = set()
        result = []

        def isValid(candidate):
            cnt = 0
            for ch in candidate:
                if ch == "(":
                    cnt += 1
                elif ch == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        while queue:
            candidate = queue.popleft()
            if isValid(candidate):
                result.append(candidate)
            elif result:
                pass
            else:
                for idx, ch in enumerate(candidate):
                    if ch not in "()":
                        continue
                    if idx == 0 or ch != candidate[idx - 1]:
                        news = candidate[:idx] + candidate[idx + 1:]
                        if news not in visited:
                            visited.add(news)
                            queue.append(candidate[:idx] + candidate[idx + 1:])
        return result
