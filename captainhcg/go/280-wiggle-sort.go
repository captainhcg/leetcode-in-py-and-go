func wiggleSort(nums []int)  {
    for idx := 1; idx < len(nums); idx += 1{
        if (idx & 1 == 1) && (nums[idx-1] > nums[idx]) {
            nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
        } 
        if (idx & 1 == 0) && (nums[idx-1] < nums[idx]) {
            nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
        }
    }
}
