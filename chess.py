#!/usr/bin/python
class Board:
    def __init__(self):
        self.board = self.createBoard()
    def createBoard(self):
        board = [["  "] * 8 for a in range(8)] # empty board

        pawn1 = Pawn(0, 1, "Pawn", "Black")
        board[0][0] = pawn1.team + pawn1.name
        board[7][7] = "WR"
        return board
    def printBoard(self):
        for i in self.board:
            print(i)

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
    def move(self):
        x = 1

class Bishop(Piece):
    def move(self):
        x = 1

class Knight(Piece):
    def move(self):
        x = 1

class Queen(Piece):
    def move(self):
        x = 1

class King(Piece):
    def move(self):
        x = 1
        
def main():
    x = Board()
    print("1")
    x.printBoard()
if __name__ == "__main__":
    main()