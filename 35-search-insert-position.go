func searchInsert(nums []int, target int) int {
    if len(nums) == 0{
        return 0
    }
    pos := helper(nums, 0, len(nums)-1, target)
    if nums[pos] == target{
        return pos
    } else if nums[pos] < target{
        return pos + 1
    } else{
        return pos
    }
    
}

func helper(nums []int, start, end, target int) int{
    if start == end{
        return start
    }
    mid := (start + end) / 2
    if nums[mid] == target{
        return mid
    } else if nums[mid] > target{
        return helper(nums, start, mid, target)
    } else {
        return helper(nums, mid+1, end, target)
    }
}
