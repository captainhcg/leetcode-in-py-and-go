func isValid(s string) bool {
    stack := make([]byte, len(s))
    cmap := map[byte]byte{
        ')': '(',
        '}': '{',
        ']': '[',
    }
    height := 0
    for idx := 0; idx < len(s); idx += 1{
        ch := s[idx]
        if ch == '[' || ch == '(' || ch == '{' {
            stack = append(stack, ch)    
            height += 1
        } else {
            if len(stack) == 0{
                return false
            }
            top_element := stack[len(stack)-1]
            expected, _ := cmap[ch]
            if expected != top_element{
                return false
            }
            stack = stack[:len(stack)-1]
            height -= 1
        }
    }
    return height == 0
}
