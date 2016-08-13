func getRow(rowIndex int) []int {
    row := []int{1}
    for idx := 1; idx <= rowIndex; idx += 1{
        for jdx := len(row)-1; jdx > 0; jdx -= 1{
            row[jdx] = row[jdx] + row[jdx-1]
        }
        row = append(row, 1)
    }
    return row
}
