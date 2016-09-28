var mat [][]bool

func isMatch(s string, p string) bool {
	mat = make([][]bool, len(s)+1)
	for row := 0; row <= len(s); row += 1 {
		mat[row] = make([]bool, len(p)+1)
	}
	ss := "#" + s
	pp := "#" + p
	for i := 0; i <= len(s); i++ {
		for j := 0; j <= len(p); j++ {
			if i == 0 && j == 0 {
				mat[i][j] = true
			} else if i == 0 {
				if j >= 2 && pp[j] == '*' {
					mat[i][j] = mat[i][j-2]
				} else {
					mat[i][j] = false
				}
			} else if j == 0 {
				mat[i][j] = false
			} else {
				if ss[i] == pp[j] || pp[j] == '.' {
					mat[i][j] = mat[i-1][j-1]
				} else if pp[j] == '*' && j >= 2 {
					if mat[i][j-2] == true || mat[i][j-1] == true {
						mat[i][j] = true
					} else if (ss[i] == pp[j-1] || pp[j-1] == '.') && mat[i-1][j] == true {
						mat[i][j] = true
					}
				} else {
					mat[i][j] = false
				}
			}
		}
	}
	return mat[len(s)][len(p)]
}
