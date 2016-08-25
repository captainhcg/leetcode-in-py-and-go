class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        indices = [0] * 3
        primes = [2, 3, 5]
        
        while len(uglys) < n:
            next = min(primes[i] * uglys[indices[i]] for i in xrange(3))
            if next / uglys[indices[0]] == 2:
                indices[0] += 1
            if next / uglys[indices[1]] == 3:
                indices[1] += 1
            if next / uglys[indices[2]] == 5:
                indices[2] += 1
                
            if uglys[-1] == next:
                continue
            
            uglys.append(next)
            
        return uglys[n - 1]
