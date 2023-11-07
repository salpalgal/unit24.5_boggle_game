from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"]="HELLO"

@app.route("/")
def homepage():
    board= boggle_game.make_board()
    session["board"] = board
    played = session.get("played",0)
    highscore = session.get("highscore",0)
    return render_template("homepage.html" , board = board, played=played, highscore=highscore)

@app.route("/check-word")
def checking():
    word = request.args["word"]
    board= session["board"]
    checked = boggle_game.check_valid_word(board,word)
    result = {"result":checked}
    return jsonify(result)

@app.route("/post-score", methods=["POST"])
def post_score():
    points= request.json["points"]
    highscore = session.get("highscore",0)
    played= session.get("played",0)
    session["played"] = played+1
    if points > highscore:
        session["highscore"] = points
        return jsonify({"brokeRecord": points})
    else:
        return jsonify({"points": points})

    # return jsonify(brokeRecord = score > highscore)
