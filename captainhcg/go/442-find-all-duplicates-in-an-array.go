func abs(num int) int{
    if num >= 0{
        return num
    }
    return -num
} 

func findDuplicates(nums []int) []int {
    ret := make([]int, 0)
    for _, num := range nums{
        newIdx := abs(num) - 1
        if nums[newIdx] < 0 {
            ret = append(ret, newIdx + 1)
        } else {
            nums[newIdx] = -nums[newIdx]
        }
    }
    return ret
}
