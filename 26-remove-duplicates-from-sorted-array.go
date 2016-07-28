func removeDuplicates(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    st, ed := 1, 1
    for ed < len(nums) {
        if nums[ed] != nums[ed-1] {
            nums[st] = nums[ed]
            st += 1
        }
        ed += 1
    }
    return st
}
