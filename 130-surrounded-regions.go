func solve(board [][]byte)  {
    flipBorder(board)
    filpBack(board)
}

func flipBorder(board [][]byte){
    for y := 0; y < len(board); y += 1{
        for x := 0; x < len(board[0]); x += 1{
            if (y == 0 || x == 0 || y == len(board) -1 || x == len(board[0]) -1) && board[y][x] == 'O' {
                filpCell(board, y, x)
            }
        }
    }
}

func filpCell(board [][]byte, y, x int){
    if y >= 0 && x >= 0 && y < len(board) && x < len(board[0]){
        if board[y][x] == 'O'{
            board[y][x] = '1'
            filpCell(board, y, x+1)
            filpCell(board, y, x-1)
            filpCell(board, y+1, x)
            filpCell(board, y-1, x)
        }
    }
}

func filpBack(board [][]byte){
    for y := 0; y < len(board); y += 1{
        for x := 0; x < len(board[0]); x += 1{
            if board[y][x] == '1'{
                board[y][x] = 'O'
            } else if board[y][x] == 'O'{
                board[y][x] = 'X'
            }
        }
    } 
}
