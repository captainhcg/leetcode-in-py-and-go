func singleNumber(nums []int) int {
    arr := make([]int, 32)
    for _, number := range nums {
        markCounter(arr, number)
    } 
    base := 0
    for idx := uint(0); idx < 32; idx += 1{
        if arr[idx] == 1{
            base |= (1<<idx)
        }
    }
    return base
}

func markCounter(cnt []int, number int){
    for idx := uint(0); idx < 32; idx += 1{
        if number & (1<<idx) != 0{
            cnt[idx] = (cnt[idx] + 1) % 3
        }
    }
}
