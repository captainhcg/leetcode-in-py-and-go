    def checkRow(self, board):
        for row in board:
            base = 0
            for ch in row:
                if ch == '.':
                    continue
                v = int(ch)
                if (1 << v) & base:
                    return False
                base |= (1 << v)
        return True

    def checkRect(self, board):
        for yoff in [0, 3, 6]:
            for xoff in [0, 3, 6]:
                base = 0
                for ybase in [0, 1, 2]:
                    for xbase in [0, 1, 2]:
                        ch = board[yoff+ybase][xoff+xbase]
                        if ch == '.':
                            continue
                        v = int(ch)
                        if (1 << v) & base:
                            return False
                        base |= (1 << v)
        return True
