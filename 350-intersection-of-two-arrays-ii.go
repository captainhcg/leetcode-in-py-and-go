func intersect(nums1 []int, nums2 []int) []int {
    sort.Ints(nums1)
    sort.Ints(nums2)
    p1 := 0
    p2 := 0
    res := []int{}
    for p1 < len(nums1) && p2 < len(nums2) {
        n1 := nums1[p1]
        n2 := nums2[p2]
        if n1 == n2 {
            res = append(res, n1)
            p1 += 1
            p2 += 1
        } else if (n1 > n2) {
            p2 += 1
        } else {
            p1 += 1
        }
    }
    return res
}
