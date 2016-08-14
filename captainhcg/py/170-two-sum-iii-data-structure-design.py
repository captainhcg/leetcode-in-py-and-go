class TwoSum(object):
    def __init__(self):
        self.counter = {}

    def add(self, number):
        self.counter[number] = self.counter.get(number, 0) + 1
        
    def find(self, value):
        for k in self.counter:
            target = value - k
            if target == k:
                if self.counter[k] >= 2:
                    return True
            elif (target in self.counter):
                return True
        return False
