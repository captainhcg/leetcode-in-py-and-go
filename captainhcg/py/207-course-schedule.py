class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inline = [0] * numCourses
        outline = [[] for _ in xrange(numCourses)]
        for o, i in prerequisites:
            inline[i] += 1
            outline[o].append(i)
        
        dq = []
        for idx, v in enumerate(inline):
            if not v:
                dq.append(idx)
                
        courses = 0
        while dq:
            course = dq.pop()
            courses += 1
            for o in outline[course]:
                inline[o] -= 1
                if inline[o] == 0:
                    dq.append(o)
        
        return courses == numCourses
