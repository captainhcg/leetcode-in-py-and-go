func reverse(x int) int {
    if x == 0 {
        return 0
    }
    neg := (x < 0)
    if neg {
        x = -x
    }
    ret := 0
    for ; x > 0; {
        ret = ret * 10 + x % 10
        x = x / 10
    }
    if neg {
        ret = -ret
    }
    if ret > 2147483647 || ret < -2147483648 {
        ret = 0
    }
    return ret
}
