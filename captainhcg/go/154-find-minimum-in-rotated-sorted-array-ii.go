func findMin(nums []int) int {
    l := 0
    r := len(nums) - 1
    for l <= r{
        if l == r{
            return nums[l]
        }
        mid := (l + r) / 2
        if nums[mid] < nums[r]{
            r = mid
        } else if nums[r] < nums[mid]{
            l = mid + 1
        } else {
            r -= 1
        }
    }
    return -1
}
