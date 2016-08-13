func containsDuplicate(nums []int) bool {
    set := make(map[int]bool)
    for _, num := range nums{
        _, ok := set[num]
        if ok {
            return true
        }
        set[num] = true
    }
    return false
}
