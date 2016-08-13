func findPeakElement(nums []int) int {
    if len(nums) == 1{
        return 0
    }
    left, right := 0, len(nums) - 1
    for left <= right{
        mid := (left + right) / 2
        v := nums[mid]
        if left == right{
            return left
        } else if v < nums[mid+1] {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}
