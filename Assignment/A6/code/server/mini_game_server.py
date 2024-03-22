# a mini web server that serves a simple game

from flask import Flask, request, jsonify
# from game.tictactoe import tictactoe
import json



app = Flask(__name__)

# a staic page that serves the game, using html template
@app.route('/')
def index():
    template = open('tictactoe.html').read()
    return template

@app.route('/game', methods=['POST'])
def game():
    data = request.get_json()
    print("data:", data)
    # game = tictactoe()
    # game.play(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
    
