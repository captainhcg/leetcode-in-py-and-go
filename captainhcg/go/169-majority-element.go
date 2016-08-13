func majorityElement(nums []int) int {
    ele := nums[0]
    cnt := 1
    for _, e := range nums[1:]{
        if ele == e {
            cnt += 1
        } else if cnt == 0 {
            ele = e
            cnt = 1
        } else {
            cnt -= 1
        }
    }
    return ele
}
