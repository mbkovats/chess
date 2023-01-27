from chess.Pieces.GamePiece import GamePiece
class Knight(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
    def ifPossible(self, move, board):
        if((move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8)):
            pass
        elif move.occupied:
            if move.piece.white == self.piece.white:
                return "FAIL"
        elif(abs(move.x - self.location.x) == 2 and abs(move.y - self.location.y) == 1):
            return "PASS"
        elif(abs(move.y - self.location.y) == 2 and abs(move.x - self.location.x) == 1):
            return "PASS"
        return "FAIL"