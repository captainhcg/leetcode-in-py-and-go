func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}

func threeSumClosest(nums []int, target int) int {
    sum := nums[0] + nums[1] + nums[2]
    min_diff := abs(sum - target)
    sort.Ints(nums)
    for idxa, va := range nums {
        idxb := idxa + 1
        idxc := len(nums) - 1
        for idxb < idxc {
            vb := nums[idxb]
            vc := nums[idxc]
            diff := va + vb + vc - target
            if abs(diff) < min_diff{
                min_diff = abs(diff)
                sum = va + vb + vc
            }
            if diff < 0 {
                idxb += 1
            } else {
                idxc -= 1
            }
        }
    }
    return sum
}
