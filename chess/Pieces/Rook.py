from chess.Pieces.GamePiece import GamePiece
class Rook(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
        self.moved = "FAIL"
    def ifPossible(self, move, board):
        if((move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8)):
            pass
        if(move.occupied):
                if move.piece.white == self.white:
                    return "FAIL"
        elif(move.x == self.location.x or move.y == self.location.y):
            if move.x >= self.location.x and move.y >= self.location.y:
                for j in range(self.location.y - 1, move.y):
                    if board[self.location.x - 1][j].location.occupied:
                        return "FAIL"
                for i in range(self.location.x - 1, move.x):
                    for j in range(self.location.y - 1, move.y):
                        if i == self.location.x - 1 or j == self.location.y - 1:
                            if board[i][j].location.occupied:
                                return "FAIL"
            elif move.x <= self.location.x and move.y >= self.location.y:
                for j in range(self.location.y - 1, move.y):
                    if board[self.location.x - 1][j].location.occupied:
                        return "FAIL"
                for i in range(move.x - 1, self.location.x):
                    for j in range(self.location.y - 1, move.y):
                        if i == self.location.x - 1 or j == self.location.y - 1:
                            if board[i][j].location.occupied:
                                return "FAIL"
            elif move.x >= self.location.x and move.y <= self.location.y:
                for j in range(move.y - 1, self.location.y):
                    if board[self.location.x - 1][j].location.occupied:
                        return "FAIL"
                for i in range(self.location.x - 1, move.x):
                    for j in range(move.y - 1, self.location.y):
                        if i == self.location.x - 1 or j == self.location.y - 1:
                            if board[i][j].location.occupied:
                                return "FAIL"
            elif move.x <= self.location.x and move.y <= self.location.y:
                for j in range(move.y - 1, self.location.y):
                    if board[self.location.x - 1][j].location.occupied:
                        return "FAIL"
                for i in range(move.x - 1, self.location.x):
                    for j in range(move.y - 1, self.location.y):
                        if i == self.location.x - 1 or j == self.location.y - 1:
                            if board[i][j].location.occupied:
                                return "FAIL"
            return "PASS"
        return "FAIL"