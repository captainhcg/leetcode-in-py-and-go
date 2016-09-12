func maxRotateFunction(A []int) int {
    s := sum(A...)
    ret := 0
    for idx, v := range(A){
        ret += idx * v
    }
    cur := ret
    for idx := 1; idx < len(A); idx += 1{
        cur = cur + s - A[len(A) - idx] * len(A)
        ret = max(ret, cur)
    }
    return ret
}

func max(v1, v2 int) int{
    if v1 > v2{
        return v1
    }
    return v2
}

func sum(arr ...int) int {
    ret := 0
    for _, n := range arr{
        ret += n
    }
    return ret
}
