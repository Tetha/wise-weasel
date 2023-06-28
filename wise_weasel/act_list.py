
from flask import render_template, request

from wise_weasel.model import get_data_loader
from . import app

@app.route("/hints/<game>/acts")
def list_acts(game):
    loader = get_data_loader()
    help = loader.load_help_for_game(game)
    if help is None:
        return "The weasel doesn't know much about this game", 404

    last_solved_act_id = int(request.args.get('lastSolvedAct', '-1'))

    seen_acts = []
    for act in help.acts:
        if act.index <= last_solved_act_id:
            seen_acts.append(act)
        else:
            seen_acts.append(act)
            break

    max_act_id = max(help.acts, key=lambda a: a.index).index

    return render_template("act_list.html.j2",
                           game=game,
                           seen_acts=seen_acts,
                           max_act_id=max_act_id)