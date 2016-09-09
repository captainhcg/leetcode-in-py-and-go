class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return abs(nums[1] - nums[0])

        min_number, max_number = min(nums), max(nums)
        bucket = [dict() for _ in xrange(len(nums) + 1)]
        bucket_size = (max_number - min_number) / len(bucket) + 1

        def get_bucket(n):
            return (n - min_number) / bucket_size

        for n in nums:
            bucket_idx = get_bucket(n)
            if not bucket[bucket_idx]:
                bucket[bucket_idx] = {"min": n, "max": n}
            else:
                bucket[bucket_idx]["max"] = max(bucket[bucket_idx]["max"], n)
                bucket[bucket_idx]["min"] = min(bucket[bucket_idx]["min"], n)
        max_gap = 0
        last_n = min_number
        for b in bucket:
            if not b:
                continue
            max_gap = max(b["min"] - last_n, max_gap)
            last_n = b["min"]
            max_gap = max(b["max"] - last_n, max_gap)
            last_n = b["max"]

        return max_gap
