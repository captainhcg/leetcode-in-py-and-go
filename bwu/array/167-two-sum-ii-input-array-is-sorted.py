class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        if n < 2:
            return []
        head, tail = 0, n - 1
        while head < tail:
            tmp = numbers[head] + numbers[tail]
            if tmp == target:
                return [head + 1, tail + 1]
            elif tmp < target:
                head += 1
            else:
                tail -= 1
                
        return []
