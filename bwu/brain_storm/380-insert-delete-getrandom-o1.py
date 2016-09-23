from random import randint

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        
        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        
        to_remove_idx = self.map[val]
        self.map.pop(val)
        if to_remove_idx != len(self.nums) - 1:
            to_swap = self.nums[-1]
            self.nums[-1], self.nums[to_remove_idx] = self.nums[to_remove_idx], self.nums[-1]
            self.map[to_swap] = to_remove_idx
        self.nums = self.nums[:-1]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[randint(0, len(self.nums)-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
