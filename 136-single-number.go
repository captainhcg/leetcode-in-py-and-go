func singleNumber(nums []int) int {
    if len(nums) == 1{
        return nums[0]
    }
        
    mark := nums[0]
    for _, num := range nums[1:]{
        mark = mark ^ num
    }
    return mark
}
