class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        ugly = [1]
        length = len(primes)
        indices = [0] * length
        seen = set()
        h = []
        for i in xrange(length):
            h.append((primes[i], i))
        
        while len(ugly) < n:
            u, idx = heapq.heappop(h)
            indices[idx] += 1
            if u not in seen:
                ugly.append(u)
                seen.add(u)
            
            heapq.heappush(h, (primes[idx] * ugly[indices[idx]], idx))

        return ugly[-1]
