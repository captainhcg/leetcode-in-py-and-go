func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }
    rows := [][]byte{}
    for i := numRows; i > 0; i -= 1 {
        rows = append(rows, []byte{})
    }
    down := true
    line := 0
    for idx := 0; idx < len(s); idx += 1 {
        ch := s[idx]
        rows[line] = append(rows[line], ch)
        if line == 0 {
            down = true
        } else if line == numRows - 1 {
            down = false
        }
        if down {
            line += 1
        } else {
            line -= 1
        }
    }
    res := ""
    for _, row := range rows {
        res += string(row)
    }
    return res
}
