class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in xrange(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append('FizzBuzz')
            elif i % 3 == 0:
                ret.append('Fizz')
            elif i % 5 == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
                
        return ret
