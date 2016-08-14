func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
    // k: index diff; t: value diff
    // store value in dict where the index is the bucket of index
    if t < 0{
        return false
    }
    buckets, bucket_size := make(map[int]int), t + 1
    for idx, v := range nums{
        bucket := getBucketIdx(v, bucket_size)
        _, valid := buckets[bucket]
        if valid{
            return true
        }
        preIdx, valid := buckets[bucket-1]
        if valid && abs(nums[preIdx]-nums[idx]) <= t{
            return true   
        }
        nextIdx, valid := buckets[bucket+1]
        if valid && abs(nums[nextIdx]-nums[idx]) <= t{
            return true   
        }

        buckets[bucket] = idx
        if idx >= k{
            bucket_to_delete := getBucketIdx(nums[idx-k], bucket_size)
            delete(buckets, bucket_to_delete)
        }
    }
    return false
}

func getBucketIdx(v, bucket_size int) int{
    if v > 0 {
        return (v -1) / bucket_size
    } else {
        return v / bucket_size - 1
    }
}

func abs(a int) int{
    if a > 0{
        return a
    } else {
        return -a
    }
}
