func longestPalindrome(s string) string {
    if len(s) == 0{
        return ""
    }
    if len(s) == 1{
        return s
    }
    start, end, maxlen := 0, 0, 0
    for idx := 0; idx < len(s); idx += 1{
        left, right := idx, idx
        for right + 1 < len(s) && s[right + 1] == s[left]{
            right += 1
            idx += 1
        }
        for left - 1 >= 0 && right + 1 < len(s) && s[left - 1] == s[right + 1]{
            left -= 1
            right += 1
        }
        if(right - left + 1 > maxlen){
            maxlen = right - left + 1
            start, end = left, right
        }
    }
    return s[start: end+1]
}
