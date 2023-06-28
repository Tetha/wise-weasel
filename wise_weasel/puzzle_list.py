
from flask import render_template

from wise_weasel.model import get_data_loader
from . import app

@app.route("/v1/hints/<game>/act/<act_name>/puzzles")
def list_puzzles(game, act_name):
    loader = get_data_loader()
    help_for_game = loader.load_help_for_game(game)
    if help_for_game is None:
        return "The weasel doesn't know much about this game", 404

    current_act = None
    for act in help_for_game.acts:
        if act.name == act_name:
            current_act = act
            break
    else:
        return "The weasel doesn't know this act in this game", 404

    return render_template('puzzle_list.html.j2', game=game, act=current_act)