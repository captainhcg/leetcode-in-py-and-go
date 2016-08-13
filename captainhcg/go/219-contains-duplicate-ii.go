func containsNearbyDuplicate(nums []int, k int) bool {
    m := make(map[int]int)
    for idx, n := range nums{
        lastidx, valid := m[n]
        if valid{
            if idx - lastidx <= k{
                return true
            }
        }
        m[n] = idx
    }
    return false
}
