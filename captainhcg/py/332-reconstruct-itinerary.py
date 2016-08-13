class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        ret = []
        itmap = collections.defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            itmap[f].append(t)
            
        def dfs(f_city):
            while itmap[f_city]:
                t_city = itmap[f_city].pop()
                dfs(t_city)
            ret.append(f_city)
                
        dfs("JFK")
        return ret[::-1]
