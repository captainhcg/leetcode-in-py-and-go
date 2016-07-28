func removeElement(nums []int, val int) int {
    if len(nums) == 0 {
        return 0
    }
    st, ed := 0, 0
    for ed < len(nums){
        if nums[ed] != val {
            nums[st], nums[ed] = nums[ed], nums[st]
            st += 1
        }
        ed += 1
    }
	fmt.Println(nums)
    return st
}
