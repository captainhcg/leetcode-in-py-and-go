func romanToInt(s string) int {
    cmap := map[byte]int{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    sum := 0
    for idx := 0; idx < len(s); idx += 1{
        ch := s[idx]
        if idx == 0 {
            sum += cmap[ch]
        } else {
            this_v := cmap[ch]
            last_v := cmap[s[idx-1]]
            sum += this_v
            if this_v > last_v {
                sum -= last_v * 2
            }
        }
    }
    return sum
}
