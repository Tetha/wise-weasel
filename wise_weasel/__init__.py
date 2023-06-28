from flask import Flask, g

from wise_weasel.model import DummyLoader

app = Flask(__name__)

@app.before_request
def before_request():
  g.loader = DummyLoader()

import wise_weasel.act_list
import wise_weasel.game_list
import wise_weasel.puzzle_list