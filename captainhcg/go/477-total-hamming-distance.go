func totalHammingDistance(nums []int) int {
    cnt := 0
    for i := uint32(0); i < 32; i += 1{
        zero, one := 0, 0
        for _, number := range nums{
            if (number >> i) & 1 == 0 {
                one += 1
            } else {
                zero += 1
            }
        }
        cnt += zero * one
    }
    return cnt
}
