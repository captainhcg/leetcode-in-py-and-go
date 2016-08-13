var res []string

func generateParenthesis(n int) []string {
    res = make([]string, 0)
    genHelper(n, n, "")
    return res
}

func genHelper(left, right int, cur string){
    if left == 0 && right == 0 {
        res = append(res, cur)
        return
    }
    if left == 0 {
        genHelper(left, right - 1, cur + ")")
    } else if left < right {
        genHelper(left, right - 1, cur + ")")
        genHelper(left - 1, right, cur + "(")
    } else if left == right {
        genHelper(left - 1, right, cur + "(")
    }
}
