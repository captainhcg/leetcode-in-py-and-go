func isMatch(s string, p string) bool {
    idx, jdx, last_idx, last_star := 0, 0, -1, -1
    for idx < len(s){
        if jdx < len(p) && (s[idx] == p[jdx] || p[jdx] == '?') {
            idx += 1
            jdx += 1
            continue
        }
        if jdx < len(p) && p[jdx] == '*' {
            last_idx = idx
            last_star = jdx
            jdx += 1
            continue
        }
        if last_star >= 0 {
            jdx = last_star 
            last_idx += 1
            idx = last_idx
            continue
        }
        return false
    }
    for jdx < len(p) && p[jdx] == '*'{
        jdx += 1
    }
    return jdx == len(p)
}
