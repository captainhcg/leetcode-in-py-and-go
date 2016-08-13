func removeDuplicates(nums []int) int {
    lastIdx, preVal, cnt := 0, 0, 0
    for idx := 0; idx < len(nums); idx += 1{
        v := nums[idx]
        if v != preVal{
            cnt = 1
            preVal = v
        } else {
            cnt += 1
        }
        if cnt <= 2{
            nums[lastIdx] = v
            lastIdx += 1
        }
    }
    return lastIdx
}
