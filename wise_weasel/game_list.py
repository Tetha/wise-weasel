
from flask import render_template

from wise_weasel.model import get_data_loader
from . import app

@app.route("/v1/games")
def list_games():
    loader = get_data_loader()

    games = loader.load_game_list()

    return render_template("game_list.html.j2", games=games)