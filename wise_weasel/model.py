from typing import Protocol
from flask import g
from pydantic import BaseModel


class Game(BaseModel):
    name: str

class Act(BaseModel):
    name: str
    index: int

class HelpForGame(BaseModel):
    acts: list[Act]


class Loader(Protocol):
    def load_game_list(self) -> list[Game]: ...
    def load_help_for_game(self, game: str) -> HelpForGame: ...

def get_data_loader() -> Loader:
    return g.loader

class DummyLoader:
    def __init__(self):
        self.games = {
            "Irony Curtain: From Matryoshka with Love": HelpForGame(
                acts = [
                    Act(name="Proloque", index=0),
                    Act(name="The Call", index=10),
                    Act(name="Matryoshka", index=20),
                    Act(name="The secret meeting", index=30),
                    Act(name="Vlad", index=40)
                ]
            )
        }

    def load_help_for_game(self, game: str) -> HelpForGame:
        return self.games.get(game, None)

    def load_game_list(self) -> list[Game]:
        return [
            Game(name="The Day of the Tentacle"),
            Game(name="Irony Curtain: From Matryoshka with Love"),
            Game(name="Technobabylon"),
        ]