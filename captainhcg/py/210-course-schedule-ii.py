class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        from collections import deque, defaultdict
        q = deque()
        inbound = defaultdict(set)
        outbound = defaultdict(set)
        ret = []
        for course, pre in prerequisites:
            outbound[pre].add(course)
            inbound[course].add(pre)
        [q.append(c) for c in xrange(numCourses) if not inbound[c]]
        while q:
            c = q.popleft()
            ret.append(c)
            for next_course in outbound[c]:
                inbound[next_course].remove(c)
                if not inbound[next_course]:
                    q.append(next_course)
        return ret if len(ret) == numCourses else []
