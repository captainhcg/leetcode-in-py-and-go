func canConstruct(ransomNote string, magazine string) bool {
    mmap := makeMap(magazine)
    nmap := makeMap(ransomNote)
    for ch := range nmap{
        cnt, valid := mmap[ch]
        if valid == false{
            return false
        }
        if cnt < nmap[ch]{
            return false
        }
    }
    return true
}

func makeMap(s string) map[rune]int{
    m := make(map[rune]int)
    for _, ch := range s{
        cnt, valid := m[ch]
        if valid{
            m[ch] = cnt + 1
        } else {
            m[ch] = 1
        }
    }
    return m
}
