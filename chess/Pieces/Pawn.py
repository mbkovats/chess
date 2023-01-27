from chess.Pieces.GamePiece import GamePiece
class Pawn(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
        self.moved = "FAIL"
    def ifPossible(self, move, board):
        if((move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8)):
            pass
        elif move.occupied:
            if move.piece.white == self.white:
                return "FAIL"
            else:
                if move.x == self.location.x + 1 and move.y == self.location.y + 1:
                    return "PASS"
        elif(move.x != self.location.x):
            pass
        elif(self.white == "PASS"):
            if(self.moved):
                if(move.y == self.location.y + 1):
                    return "PASS"
            else:
                if(move.y == self.location.y + 1 or move.y == self.location.y + 2):
                    return "PASS"
        else:
            if(self.moved):
                if(move.y == self.location.y - 1):
                    return "PASS"
            else:
                if(move.y == self.location.y - 1 or move.y == self.location.y - 2):
                    return "PASS"
        return "FAIL"