class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        arr1 = nums[:(len(nums)+1)/2]
        arr2 = nums[(len(nums)+1)/2:]
        ret = []
        for n1, n2 in zip(arr1[::-1], arr2[::-1]):
            ret.append(n1)
            ret.append(n2)
        if len(arr1) > len(arr2):
            ret.append(arr1[0])
        for idx, n in enumerate(ret):
            nums[idx] = n
