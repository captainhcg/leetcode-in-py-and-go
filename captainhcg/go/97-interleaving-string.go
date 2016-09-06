func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s3) != len(s1)+len(s2) {
		return false
	}
	mat := make([][]bool, len(s1)+1)
	for idx := 0; idx <= len(s1); idx += 1 {
		mat[idx] = make([]bool, len(s2)+1)
	}
	mat[0][0] = true

	for row := 0; row <= len(s1); row += 1 {
		for col := 0; col <= len(s2); col += 1 {
			if row == 0 && col == 0 {
				// do nothing
			} else if row == 0 {
				if mat[0][col-1] == true && s2[col-1] == s3[col-1] {
					mat[0][col] = true
				} else {
					mat[0][col] = false
				}
			} else if col == 0 {
				if mat[row-1][0] == true && s1[row-1] == s3[row-1] {
					mat[row][0] = true
				} else {
					mat[row][0] = false
				}
			} else {
				if s1[row-1] == s3[row+col-1] && mat[row-1][col] == true {
					mat[row][col] = true
				} else if s2[col-1] == s3[row+col-1] && mat[row][col-1] == true {
					mat[row][col] = true
				} else {
					mat[row][col] = false
				}
			}
		}
	}
	return mat[len(s1)][len(s2)]
}
