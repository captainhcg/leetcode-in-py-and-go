func maxSubArray(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    max := nums[0]
    for _, n := range(nums){
        if n > max{
            max = n
        }
    }
    if max < 0{
        return max
    } 
    
    tmp := 0
    for _, n := range(nums){
        if tmp + n > 0{
            tmp = tmp + n
            if tmp > max{
                max = tmp
            }
        } else {
            tmp = 0
        }
    }
    return max
}
