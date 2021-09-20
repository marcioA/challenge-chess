from flask import Flask, request

# from chess import insertPlay

app = Flask("Chess")

# The api should:
# ● receive the piece type/name and the color and return the piece id; --> Ok 
# ● receive cell coordinate (in Algebraic notation) and the piece id and return an array
# with all possible locations where the knight can move within 2 turns.

listPiece = []

# [id, piece, initPosition, color, actualPosition]

# black
listPiece.append(["010", "pawns", "A7", "black", "A7"])
listPiece.append(["011", "pawns", "B7", "black", "B7"])
listPiece.append(["012", "pawns", "C7", "black", "C7"])
listPiece.append(["013", "pawns", "D7", "black", "D7"])
listPiece.append(["014", "pawns", "E7", "black", "E7"])
listPiece.append(["015", "pawns", "F7", "black", "F7"])
listPiece.append(["016", "pawns", "G7", "black", "G7"])
listPiece.append(["017", "pawns", "H7", "black", "H7"]) 

listPiece.append(["110", "rooks", "H8", "black", "A8"])
listPiece.append(["111", "rooks", "H8", "black", "H8"])

listPiece.append(["210", "knights", "B8", "black", "B8"])
listPiece.append(["211", "knights", "G8", "black", "G8"])

listPiece.append(["310", "bishops", "C8", "black", "C8"])
listPiece.append(["311", "bishops", "F8", "black", "F8"])

listPiece.append(["410", "queen", "D8", "black", "D8"])
listPiece.append(["411", "king", "E8", "black", "E8"])

# white
listPiece.append(["020", "pawns", "A7", "white", "A7"])
listPiece.append(["021", "pawns", "B7", "white", "B7"])
listPiece.append(["022", "pawns", "C7", "white", "C7"])
listPiece.append(["023", "pawns", "D7", "white", "D7"])
listPiece.append(["024", "pawns", "E7", "white", "E7"])
listPiece.append(["025", "pawns", "F7", "white", "F7"])
listPiece.append(["026", "pawns", "G7", "white", "G7"])
listPiece.append(["027", "pawns", "H7", "white", "H7"]) 

listPiece.append(["120", "rooks", "H8", "white", "A8"])
listPiece.append(["121", "rooks", "H8", "white", "H8"])

listPiece.append(["220", "knights", "B8", "white", "B8"])
listPiece.append(["221", "knights", "G8", "white", "G8"])

listPiece.append(["320", "bishops", "C8", "white", "C8"])
listPiece.append(["321", "bishops", "F8", "white", "F8"])

listPiece.append(["420", "queen", "D8", "white", "D8"])
listPiece.append(["421", "king", "E8", "white", "E8"])

@app.route("/played", methods=["POST"])
def findID():

    body = request.get_json()

    playedPiece = {"piece": body["piece"], "color": body["color"]}

    for p in listPiece:
        if p[1] == playedPiece["piece"]:
            if p[3] == playedPiece["color"]:
                pieceId = p[0]

    return  str(pieceId)

@app.route("/possiblesPlay", methods=["POST"])
def possiblePlay():

    body = request.get_json()

    possiblePlay = {"id": body["id"], "coordinate": body["coordinate"]}

    if possiblePlay["id"]  in (210, 211, 221, 220 ):
        # movimento cavalo
    else if possiblePlay["id"] in (320, 321,  310, 311)



    return  str(possiblePlay)


app.run()