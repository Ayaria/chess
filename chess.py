#!/usr/bin/python
class Board:
    def __init__(self):
        self.board = self.createBoard()
    def createBoard(self):
        board = [["  "] * 8 for a in range(8)] # empty board
        # Initialize Black Pieces
        br1 = Rook(0, 0, "R", "B")
        bn1 = Knight(0, 1, "N", "B")
        bb1 = Bishop(0, 2, "B", "B")
        bq = Queen(0, 3, "Q", "B")
        bk = King(0, 4, "K", "B")
        bb2 = Bishop(0, 5, "B", "B")
        bn2 = Knight(0, 6, "N", "B")
        br2 = Rook(0, 7, "R", "B")
        bp1 = Pawn(1, 0, "P", "B")
        bp2 = Pawn(1, 1, "P", "B")
        bp3 = Pawn(1, 2, "P", "B")
        bp4 = Pawn(1, 3, "P", "B")
        bp5 = Pawn(1, 4, "P", "B")
        bp6 = Pawn(1, 5, "P", "B")
        bp7 = Pawn(1, 6, "P", "B")
        bp8 = Pawn(1, 7, "P", "B")
        board[0][0] = br1
        board[0][1] = bn1
        board[0][2] = bb1
        board[0][3] = bq
        board[0][4] = bk
        board[0][5] = bb2
        board[0][6] = bn2
        board[0][7] = br2
        board[1][0] = bp1
        board[1][1] = bp2
        board[1][2] = bp3
        board[1][3] = bp4
        board[1][4] = bp5
        board[1][5] = bp6
        board[1][6] = bp7
        board[1][7] = bp8
        # Initialize White Pieces
        wr1 = Rook(7, 0, "R", "W")
        wn1 = Knight(7, 1, "N", "W")
        wb1 = Bishop(7, 2, "B", "W")
        wq = Queen(7, 3, "Q", "W")
        wk = King(7, 4, "K", "W")
        wb2 = Bishop(7, 5, "B", "W")
        wn2 = Knight(7, 6, "N", "W")
        wr2 = Rook(7, 7, "R", "W")
        wp1 = Pawn(6, 0, "P", "W")
        wp2 = Pawn(6, 1, "P", "W")
        wp3 = Pawn(6, 2, "P", "W")
        wp4 = Pawn(6, 3, "P", "W")
        wp5 = Pawn(6, 4, "P", "W")
        wp6 = Pawn(6, 5, "P", "W")
        wp7 = Pawn(6, 6, "P", "W")
        wp8 = Pawn(6, 7, "P", "W")
        board[7][0] = wr1
        board[7][1] = wn1
        board[7][2] = wb1
        board[7][3] = wq
        board[7][4] = wk
        board[7][5] = wb2
        board[7][6] = wn2
        board[7][7] = wr2
        board[6][0] = wp1
        board[6][1] = wp2
        board[6][2] = wp3
        board[6][3] = wp4
        board[6][4] = wp5
        board[6][5] = wp6
        board[6][6] = wp7
        board[6][7] = wp8
        return board
    def printBoard(self):
        num = 8
        for i in self.board:
            print(num, end = ' ')
            num = num - 1
            for k in i:
                if issubclass(type(k), Piece):
                    print(k.team + k.name, end = ' ')
                else:
                    print(k, end = ' ')
            print("")
        print("  A  B  C  D  E  F  G  H")

class Piece(object):
    def __init__(self, x, y, name, team):
        self.x = x
        self.y = y
        self.name = name
        self.team = team
    def move(self):
        pass

class Pawn(Piece):
    def __init__(self, x, y, name, team):
        self.untouched = True
        super(Pawn, self).__init__(x, y, name, team)
    def move(self):
        x = 1

class Rook(Piece):
    def __init__(self, x, y, name, team):
        super(Rook, self).__init__(x, y, name, team)
    def move(self):
        x = 1

class Bishop(Piece):
    def __init__(self, x, y, name, team):
        super(Bishop, self).__init__(x, y, name, team)
    def move(self):
        x = 1

class Knight(Piece):
    def __init__(self, x, y, name, team):
        super(Knight, self).__init__(x, y, name, team)
    def move(self):
        x = 1

class Queen(Piece):
    def __init__(self, x, y, name, team):
        super(Queen, self).__init__(x, y, name, team)
    def move(self):
        x = 1

class King(Piece):
    def __init__(self, x, y, name, team):
        super(King, self).__init__(x, y, name, team)
    def move(self):
        x = 1
        
def main():
    x = Board()
    x.printBoard()
if __name__ == "__main__":
    main()