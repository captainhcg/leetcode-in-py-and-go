class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        if n == 0:
            return 0
        numbers = [1]
        ptrs = [0] * len(primes)
        while n > 1:
            n -= 1
            newnumber = min(numbers[ptrs[idx]] * primes[idx] for idx in xrange(len(primes)))
            numbers.append(newnumber)
            for idx, p in enumerate(primes):
                if and newnumber % p == 0:
                    ptrs[idx] += 1
        return numbers[-1]
