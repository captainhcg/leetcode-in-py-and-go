func getModifiedArray(length int, updates [][]int) []int {
    helper := make([]int, length+1)
    for _, arr := range updates{
        st, ed, offset := arr[0], arr[1], arr[2]
        helper[st] += offset
        helper[ed + 1] -= offset
    }
    mod := 0
    for idx, v := range helper{
        mod += v
        helper[idx] = mod
    }
    return helper[:length]
}
