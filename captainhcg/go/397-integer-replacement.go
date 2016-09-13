func min(v1, v2 int) int{
    if v1 < v2 {
        return v1
    }
    return v2
}

func helper(v int64) int{
    if v == 1{
        return 0  // not changed
    } else if v == 0{
        return 1  // +1
    } else if v % 2 == 0 {
        return helper(v/2) + 1
    } else {
        return min(helper(v + 1), helper(v - 1)) + 1
    }
}

func integerReplacement(n int) int {
    return helper(int64(n))
}
