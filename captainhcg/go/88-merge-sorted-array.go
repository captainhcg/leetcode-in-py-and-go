func merge(nums1 []int, m int, nums2 []int, n int) {
    pall := m + n - 1
    p1 := m-1
    p2 := n-1
    for p1 >= 0 || p2 >= 0 {
        if p1 < 0 {
            nums1[pall] = nums2[p2]
            p2 -= 1
        } else if p2 < 0 {
            nums1[pall] = nums1[p1]
            p1 -= 1
        } else {
            n1 := nums1[p1]
            n2 := nums2[p2]
            if n1 > n2 {
                nums1[pall] = nums1[p1]
                p1 -= 1
            } else {
                nums1[pall] = nums2[p2]
                p2 -= 1
            }
        }
        pall -= 1
    }
}
