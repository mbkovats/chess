from chess.Pieces import *
from .Location import Location
from flask import Flask, render_template, request
from json import dumps, loads
app = Flask(__name__)
@app.route("/")
def mainhtml():
    print(request.form)
    return render_template("page.html")
board = []
for i in range(8):
    col = []
    for j in range(8):
        if i == 1:
            col.append(Pawn(j, i, True))
        elif i == 0:
            if j == 0 or j == 7:
                col.append(Rook(j, i, True))
            if j == 1 or j == 6:
                col.append(Knight(j, i, True))
            if j == 2 or j == 5:
                col.append(Bishop(j, i, True))
            if j == 3:
                col.append(Queen(j, i, True))
            if j == 4:
                col.append(King(j, i, True))
        elif i == 6:
            col.append(Pawn(j, i, False))
        elif i == 7:
            if j == 0 or j == 7:
                col.append(Rook(j, i, False))
            if j == 1 or j == 6:
                col.append(Knight(j, i, False))
            if j == 2 or j == 5:
                col.append(Bishop(j, i, False))
            if j == 3:
                col.append(Queen(j, i, False))
            if j == 4:
                col.append(King(j, i, False))
        else:
            col.append(Blank(j, i, False))
    board.append(col)
@app.route("/move", methods=["POST"])
def javascript():
    arr = request.get_json(force=True)
    print(arr)
    before = arr[0] + arr[1]
    after = arr[2] + arr[3]
    if request.method == "POST":
        beforeLoc = Location(before,Blank(0,0,True))
        piece = board[beforeLoc.x - 1][beforeLoc.y - 1]
        afterLoc = Location(after,piece)
        if(isinstance(piece,Blank)):
            return dumps("FAIL")
        else:
            if not board[afterLoc.x - 1][afterLoc.y - 1].location.occupied:
                afterLoc.occupied = True
                afterLoc.piece = board[afterLoc.x - 1][afterLoc.y - 1]
                if(piece.isPossible(afterLoc) == "FAIL"):
                    pass
                else:
                    board[beforeLoc.x - 1][beforeLoc.y - 1] = Blank(beforeLoc.x - 1, beforeLoc.y - 1, False)
                    board[afterLoc.x - 1][afterLoc.x - 1] = piece
                return dumps(piece.isPossible(afterLoc))
    return dumps("FAIL")
if __name__ == '__main__':
    app.run(debug=True)