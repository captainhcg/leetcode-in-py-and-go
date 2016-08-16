func candy(ratings []int) int {
    if len(ratings) == 0{
        return 0
    }
    candies := make([]int, len(ratings))
    candies[0] = 1
    for idx := 1; idx < len(candies); idx += 1{
        if ratings[idx] > ratings[idx-1]{
            candies[idx] = candies[idx-1] + 1
        } else {
            candies[idx] = 1
        }
    }
    for idx := len(candies) - 1; idx > 0; idx -= 1{
        if ratings[idx-1] > ratings[idx]{
            candies[idx-1] = max(candies[idx-1], candies[idx]+1)
        }
    }
    sum := 0
    for _, c := range candies{
        sum += c
    }
    return sum
}

func max(n1, n2 int) int {
    if n1 > n2{
        return n1
    } else {
        return n2
    }
}
