func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for idx, v := range(nums) {
        complement := target - v
        i, ok := m[complement]
        if ok {
            return []int{i, idx}
        }
        m[v] = idx
    }
    return []int{0, 0}  // it should never execute
}
