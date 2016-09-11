func nthUglyNumber(n int) int {
    arr := []int{1}
    p2, p3, p5 := 0, 0, 0
    for n > 1{
        un := min(arr[p2] * 2, arr[p3] * 3, arr[p5] * 5)
        arr = append(arr, un)
        if un % 2 == 0{
            p2 += 1
        }
        if un % 3 == 0{
            p3 += 1
        }
        if un % 5 == 0{
            p5 += 1
        }
        n -= 1
    }
    return arr[len(arr)-1]
}

func min(v1 int, vn ...int) (m int) {
    m = v1
    for _, v := range vn{
        if v < m{
            m = v
        }
    }
    return
}
