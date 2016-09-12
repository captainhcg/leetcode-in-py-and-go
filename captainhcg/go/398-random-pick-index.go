import (
	"math/rand"
)

type Solution struct {
    nums []int
}

func Constructor(nums []int) Solution {
    s := Solution{nums}
    return s
}

func (this *Solution) Pick(target int) int {
    selected, count := 0, 1
    for idx, v := range this.nums{
        if v != target{
            continue
        }
        if rand.Intn(count) == 0{
            selected = idx
        }
        count += 1
    }
    return selected
}
