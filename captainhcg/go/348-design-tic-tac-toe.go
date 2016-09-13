type TicTacToe struct {
    Rows [] int
    Cols [] int
    Dia int
    ADia int
    Lines int
}

func Constructor(n int) TicTacToe {
    ttt := TicTacToe{}
    ttt.Lines = n
    ttt.Rows = make([]int, ttt.Lines)
    ttt.Cols = make([]int, ttt.Lines)
    return ttt
}

func (this *TicTacToe) Move(row int, col int, player int) int {
    offset := 1
    if player == 2{
        offset = -1
    }
    this.Cols[col] += offset
    this.Rows[row] += offset
    if col == row{
        this.Dia += offset
    }
    if col + row == this.Lines - 1 {
        this.ADia += offset
    }
    if this.Cols[col] == this.Lines || this.Rows[row] == this.Lines || this.Dia == this.Lines|| this.ADia == this.Lines{
        return 1
    }else if this.Cols[col] == -this.Lines || this.Rows[row] == -this.Lines || this.Dia == -this.Lines|| this.ADia == -this.Lines{
        return 2
    }else {
        return 0
    }    
}
