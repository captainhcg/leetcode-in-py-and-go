func singleNumber(nums []int) int {
    arr := make([]int, 32)
    for _, number := range nums {
        markCounter(arr, number)
    } 
    base := int32(0)
    var idx uint
    for idx = 0; idx <= 31; idx += 1{
        if arr[idx] == 1{
            base |= (1<<idx)
        }
    }
    return int(base)
}

func markCounter(cnt []int, number int){
    var idx uint
    for idx = 0; idx <= 31; idx += 1{
        if number & (1<<idx) != 0{
            cnt[idx] = (cnt[idx] + 1) % 3
        }
    }
}
