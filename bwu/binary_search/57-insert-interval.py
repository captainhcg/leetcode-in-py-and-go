# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
            
        starts, ends = [], []
        for intv in intervals:
            starts.append(intv.start)
            ends.append(intv.end)
        
        left = self.search1(ends, newInterval.start)
        right = self.search2(starts, newInterval.end)
        print left, right
        
        if left > len(intervals) - 1:
            intervals.append(newInterval)
        elif right < 0:
            intervals.insert(0, newInterval)
        else:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)
            intervals = intervals[:left] + [newInterval] + intervals[right + 1:]
        return intervals
        
    def search1(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
                
        if nums[right] < target:
            return right + 1
        elif nums[left] < target:
            return right
        else:
            return left
            
    def search2(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
                
        if nums[left] > target:
            return left - 1
        elif nums[right] > target:
            return left
        else:
            return right
