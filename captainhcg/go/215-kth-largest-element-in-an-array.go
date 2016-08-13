func findKthLargest(nums []int, k int) int {
    return find(nums, 0, len(nums)-1, len(nums)-k)
}

func find(nums []int, lo, hi, kidx int) int {
    store, pivot := lo, nums[hi]
    for idx := lo; idx < hi; idx += 1{
        if nums[idx] < pivot{
            nums[idx], nums[store] = nums[store], nums[idx]
            store += 1
        }
    }
    nums[hi], nums[store] = nums[store], nums[hi]
    if store == kidx{
        return nums[store]
    } else if store < kidx {
        return find(nums, store+1, hi, kidx)
    } else{
        return find(nums, lo, store-1, kidx)
    }
}
