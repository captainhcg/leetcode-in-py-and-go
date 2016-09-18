class Solution(object):
    def isSelfCrossing(self, x):
        def hit(arr):
            if len(arr) <= 3:
                return False
            if len(arr) >= 4 and arr[1] <= arr[3] and arr[2] <= arr[0]:
                return True
            if len(arr) >= 5 and arr[1] == arr[3] and arr[0] + arr[4] >= arr[2]:
                return True
            if len(arr) >= 6 and arr[4] <= arr[2] and arr[0] + arr[4] >= arr[2] and arr[1] <= arr[3] and arr[1] + arr[5] >= arr[3]:
                return True
            return False
            
        for idx in xrange(len(x)):
            if hit(x[idx:idx+6]):
                return True
        return False
