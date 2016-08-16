class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (A-C) * (B-D) + (E-G) * (F-H) - self.intersection(A, B, C, D, E, F, G, H)
        
    def intersection(self, A, B, C, D, E, F, G, H):
        if C <= E or G <= A or H <= B or D <= F: 
            return 0
            
        widths = sorted([A, C, E, G])
        heights = sorted([B, D, F, H])
        return (widths[2] - widths[1]) * (heights[2] - heights[1])
