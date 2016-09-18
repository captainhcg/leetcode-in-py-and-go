class Solution(object):
    def readBinaryWatch(self, num):
        res = []

        def process(arr):
            hour = minute = 0
            for idx, h in enumerate(arr[:4][::-1]):
                if h:
                    hour += 1 << idx
            for idx, m in enumerate(arr[4:][::-1]):
                if m:
                    minute += 1 << idx
            if minute >= 60 or hour >= 12:
                return
            res.append(str(hour) + ":" + str(minute).rjust(2, "0"))

        def helper(arr, remaining, pos):
            if remaining == 0:
                process(arr)
                return
            elif pos >= len(arr):
                return

            helper(arr, remaining, pos + 1)
            arr[pos] = 1
            helper(arr, remaining-1, pos + 1)
            arr[pos] = 0

        helper([0] * 11, num, 0)
        return res
