func threeSum(nums []int) [][]int {
    if len(nums) < 3 {
        return [][] int{}
    }
    res := [][]int{}
    sort.Ints(nums)
    for idxa, va := range nums{
        if idxa > 0 && nums[idxa - 1] == va {
            continue
        }
        idxb := idxa + 1
        idxc := len(nums) - 1
        for idxb < idxc {
            if idxb > idxa + 1 && nums[idxb - 1] == nums[idxb] {
                idxb += 1
                continue
            }
            vb := nums[idxb]
            vc := nums[idxc]
            if va + vb + vc == 0 {
                res = append(res, []int{va, vb, vc})
                idxb += 1
                idxc -= 1
            } else if va + vb + vc < 0 {
                idxb += 1
            } else {
                idxc -= 1
            }
        }
    }
    return res
}
