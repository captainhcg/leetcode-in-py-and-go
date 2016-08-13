type E struct {
    number int
    count int
}
type Es []E

func (arr Es) Len() int {
    return len(arr)
}
func (arr Es) Swap(i, j int) {
    arr[i], arr[j] = arr[j], arr[i]
}
func (arr Es) Less(i, j int) bool {
    return arr[i].count > arr[j].count
}

func topKFrequent(nums []int, k int) []int {
    arr := make([]E, 0, len(nums))
    m := make(map[int]int)
    for _, num := range nums{
        m[num] += 1
    }
    for k, v := range m{
	      arr = append(arr, E{k, v})
    } 
    sort.Sort(Es(arr))
    res := make([]int, k)
    for idx := 0; idx < k; idx += 1 {
        res[idx] = arr[idx].number
    }
    return res
}
