func longestCommonPrefix(strs []string) string {
    if len(strs) == 0{
        return ""
    }
    base := strs[0]
    idx := 0
    for ; idx < len(base); idx += 1{
        for _, str := range strs {
            if len(str) > idx && base[idx] == str[idx]{
                continue
            } else {
                return base[:idx]
            }
        }
    }
    return base[:idx]
}
