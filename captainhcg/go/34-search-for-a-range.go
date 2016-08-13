func searchRange(nums []int, target int) []int {
    return []int{findLeft(nums, 0, len(nums)-1, target), findRight(nums, 0, len(nums)-1, target)}
}


func findLeft(nums []int, st, ed, t int) int {
    if st > ed{
        return -1
    }
    mid := (st + ed)/2
    if nums[mid] < t{
        return findLeft(nums, mid+1, ed, t)
    } else if nums[mid] > t{
        return findLeft(nums, st, mid-1, t)
    } else {
        if (mid == 0) || (mid > 0 && nums[mid-1] != t){
            return mid
        }
        return findLeft(nums, st, mid-1, t)
    }
}

func findRight(nums []int, st, ed, t int) int {
    if st > ed{
        return -1
    }
    mid := (st + ed)/2
    if nums[mid] < t{
        return findRight(nums, mid+1, ed, t)
    } else if nums[mid] > t{
        return findRight(nums, st, mid-1, t)
    } else {
        if (mid == len(nums) - 1) || (mid < len(nums) - 1 && nums[mid+1] != t){
            return mid
        }
        return findRight(nums, mid+1, ed, t)
    }
}
