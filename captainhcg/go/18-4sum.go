func fourSum(nums []int, target int) [][]int {
    res := [][]int{}
    sort.Ints(nums)
    for idxa := 0; idxa < len(nums) - 3; idxa += 1{
        va := nums[idxa]
        if idxa > 0 && nums[idxa - 1] == va {
            continue
        }
        for idxb := idxa + 1; idxb < len(nums) - 2; idxb += 1{
            vb := nums[idxb]
            if idxb > idxa + 1 && nums[idxb - 1] == vb {
                continue
            }
            for idxc, idxd := idxb + 1, len(nums) -1; idxc < idxd; {
                vc, vd := nums[idxc], nums[idxd]
                if idxc > idxb + 1 && nums[idxc - 1] == vc {
                    idxc += 1
                    continue
                }
                s := va + vb + vc + vd
                if s == target {
                    res = append(res, []int{va, vb, vc, vd})
                    idxd -= 1
                    idxc += 1
                } else if s < target {
                    idxc += 1
                } else {
                    idxd -= 1
                }
            }
        }
    }
    return res
}
