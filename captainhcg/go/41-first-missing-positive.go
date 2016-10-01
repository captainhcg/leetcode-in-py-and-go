func firstMissingPositive(nums []int) int {
    i := 0
    for i < len(nums){
        value := nums[i]
        if value > 0 && value <= len(nums){
            should_be_at := value - 1
            if value != nums[should_be_at]{
                nums[should_be_at], nums[i] = nums[i], nums[should_be_at]
                continue
            }
        }
        i += 1
    }
    
    for idx, v := range(nums){
        if v != idx + 1{
            return idx + 1
        }
    }

    return len(nums) + 1
}
