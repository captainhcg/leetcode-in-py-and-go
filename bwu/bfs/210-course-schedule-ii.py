class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []
            
        adjList = {}
        in_degree = {}
        
        for d, s in prerequisites:
            if d not in in_degree:
                in_degree[d] = 1
            else:
                in_degree[d] += 1
                
            if s not in adjList:
                adjList[s] = [d]
            else:
                adjList[s] += [d]
                
        queue = []
        for c in xrange(numCourses):
            if c not in in_degree:
                queue.append(c)
        
        start = 0   
        while start < len(queue):
            curr = queue[start]
            if curr in adjList:
                for n in adjList[curr]:
                    in_degree[n] -= 1
                    if in_degree[n] == 0:
                        queue.append(n)
            start += 1
            
        if len(queue) == numCourses:
            return queue
        else:
            return []
