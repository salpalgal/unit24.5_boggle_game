from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"]="HELLO"

@app.route("/")
def homepage():
    game_board= boggle_game.make_board()
    return render_template("homepage.html" , board = game_board)

@app.route("/check-word")
def checking():
    word = request.args["guess"]
    board= session["board"]
    checked = boggle_game.check_valid_word(board,word)
    result = {"result":checked}
    return jsonify(result)