class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.original = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ret = self.original[:]
        for idx in xrange(len(self.original)):
            to_swap = random.randint(idx, len(self.original) - 1)
            ret[idx], ret[to_swap] = ret[to_swap], ret[idx]
        return ret
