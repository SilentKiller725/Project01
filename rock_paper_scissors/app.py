import random
from flask import Flask, render_template, request

app=Flask(__name__)

def winner(player, computer):
    if player == computer:
        return "Tie"

    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (
            player == "paper" and computer == "rock"):
        return "You won !!!"

    else:
        return "Computer Won"


@app.route("/", methods=["GET", "POST"])
def index():
        result = None
        player_choice = None
        computer_choice = None

        if request.method == "POST":
            player_choice = request.form["choice"]
            computer_choice = random.choice(["rock", "paper", "scissor"])
            result = winner(player_choice, computer_choice)

        return render_template("index.html", result=result, player_choice=player_choice,
                               computer_choice=computer_choice)


if __name__ == "__main__":
        app.run(debug=True)