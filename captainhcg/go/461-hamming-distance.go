func hammingDistance(x int, y int) int {
    i := x ^ y
    cnt := 0
    for (i & -i) != 0 {
        i = i - i & -i;
        cnt += 1
    }
    return cnt
}
