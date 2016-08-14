func search(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        md := (left + right) / 2
        mdv := nums[md]
        if mdv == target{
            return md
        }
        if mdv > nums[right]{
            if target < mdv && nums[left] <= target{
                right = md - 1
            } else {
                left = md + 1
            }
        } else {
            if target > mdv && nums[right] >= target{
                left = md + 1
            } else {
                right = md - 1
            }
        }
    }
    return -1
}
