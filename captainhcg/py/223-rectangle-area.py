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
        inter = self.inter(A, B, C, D, E, F, G, H)
        return (A-C) * (B-D) + (E-G) * (F-H) - inter
        
    def inter(self, A, B, C, D, E, F, G, H):
        if (C - E) * (A - G) >= 0 or (D - F) * (B - H) >= 0:
            return 0
        arr1 = sorted([A, C, E, G])
        arr2 = sorted([B, D, F, H])
        return (arr1[1]-arr1[2]) * (arr2[1]-arr2[2])
