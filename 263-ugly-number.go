func isUgly(num int) bool {
    if num <= 0 {
        return false
    } else {
        return defactor(defactor(defactor(num, 5), 3), 2) == 1
    }
}

func defactor(num int, prime int) int {
    for num % prime == 0 {
        num = num / prime
    }
    return num
}
