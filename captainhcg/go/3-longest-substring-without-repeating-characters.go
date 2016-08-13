func lengthOfLongestSubstring(s string) int {
    cmap := make(map[byte]int)
    max_length, start := 0, -1
    for idx := 0; idx != len(s); idx += 1{
        ch := s[idx]
        last_idx, ok := cmap[ch]
        if ok && last_idx > start{
            start = last_idx
        }
        cmap[ch] = idx
        if idx - start > max_length{
            max_length = idx - start
        }
    }
    return max_length
}
