from random import randint

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.map = dict()
        
    def insert(self, val):
        if val in self.map:
            return False
        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        return True

    def remove(self, val):
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
        return self.nums[randint(0, len(self.nums)-1)]
