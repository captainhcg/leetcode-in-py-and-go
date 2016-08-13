func wiggleMaxLength(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    last := nums[0]
    inc := false
    inc_assigned := false
    count := 0
    for _, num := range(nums){
        if num == last{
            continue
        }
        if inc_assigned == false{
            inc = (num > last)
            inc_assigned = true
            count += 1
        } else if inc != (num > last){
            count += 1
            inc = (num > last)
        }
        last = num
    }
    return count + 1
}
