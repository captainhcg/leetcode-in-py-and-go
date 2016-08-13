func missingNumber(nums []int) int {
    for idx := 0; idx < len(nums); {
        num := nums[idx]
        if num >= len(nums){
            idx += 1
            continue
        }
        if num == idx{
            idx += 1
            continue
        }
        nums[idx], nums[num] = nums[num], nums[idx]
    }
    for idx, num := range(nums){
        if idx != num {
            return idx
        }
    }
    return len(nums)
}
