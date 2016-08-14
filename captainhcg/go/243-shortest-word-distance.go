func shortestDistance(words []string, word1 string, word2 string) int {
    last1, last2 := -1, -1
    dis := len(words)
    for idx, s := range words{
        cmp := false
        if s == word1{
            last1 = idx
            cmp = true
        } else if s == word2{
            last2 = idx
            cmp = true
        }
        if cmp && last1 >= 0 && last2 >= 0{
            dis = min(dis, abs(last1 - last2))
        }
    }
    return dis
}

func min(n1, n2 int) int{
    if n1 > n2{
        return n2
    }
    return n1
}

func abs(n int) int{
    if n >= 0{
        return n
    }
    return -n
}
