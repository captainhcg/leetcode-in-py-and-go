func sortColors(nums []int)  {
    st, ptr, ed := 0, 0, len(nums)-1
    for ptr <= ed{
        v := nums[ptr]
        if v == 0{
            swap(st, ptr, nums)
            st += 1
            ptr += 1
        } else if v == 1{
            ptr += 1
        } else {  // =2
            swap(ed, ptr, nums)
            ed -= 1
        }
    }
}

func swap(a, b int, nums []int){
    nums[a], nums[b] = nums[b], nums[a]
}
