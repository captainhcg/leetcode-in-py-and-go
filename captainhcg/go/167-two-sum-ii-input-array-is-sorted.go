func twoSum(numbers []int, target int) []int {
    left, right := 0, len(numbers) - 1
    for left < right{
        v := numbers[left] + numbers[right]
        if v == target{
            return []int{left+1, right+1}
        } else if v < target{
            left += 1
        } else{
            right -= 1
        }
    }
    return []int{-1, -1}
}
