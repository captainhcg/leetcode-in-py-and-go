class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1:
            return True
        
        in_degree = {}
        mapping = {}
        visited = set()
        
        for course_to, course_from in prerequisites:
            if course_to not in in_degree:
                in_degree[course_to] = 1
            else:
                in_degree[course_to] += 1
                
            if course_from not in mapping:
                mapping[course_from] = [course_to]
            else:
                mapping[course_from].append(course_to)
                        
        starts = []
        for i in xrange(numCourses):
            if i not in in_degree:
                starts.append(i)
                
        while starts:
            curr = starts.pop(0)
            visited.add(curr)
            if curr in mapping:
                for neighbor in mapping[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        starts.append(neighbor)
                        del in_degree[neighbor]
            
        return len(visited) == numCourses
