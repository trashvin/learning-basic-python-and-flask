# import libraries
from flask import Flask, render_template, request
from spock_app.game_engine import get_winner

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    winner = ''
    computer = ''
    player = ''
    if request.method == 'POST':
        player = request.form.get('player')
        winner, computer = get_winner(player)
    return render_template("index.html", 
                winner = winner, 
                computer = computer,
                player = player)

if __name__ == '__main__':
    app.run(debug=True)
