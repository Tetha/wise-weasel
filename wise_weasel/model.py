from typing import Protocol
from flask import g
from pydantic import BaseModel, Field


class Game(BaseModel):
    name: str

class Puzzle(BaseModel):
    name: str

class Act(BaseModel):
    name: str
    index: int
    puzzles: list[Puzzle] = Field(default_factory=list)

class HelpForGame(BaseModel):
    acts: list[Act]


class Loader(Protocol):
    def load_game_list(self) -> list[Game]: ...
    def load_help_for_game(self, game: str) -> HelpForGame: ...

def get_data_loader() -> Loader:
    return g.loader

class DummyLoader:
    def __init__(self):
        self.game_list = [
            Game(name="The Day of the Tentacle"),
            Game(name="Irony Curtain: From Matryoshka with Love"),
            Game(name="Technobabylon"),
        ]

        self.games = {
            "Irony Curtain: From Matryoshka with Love": HelpForGame(
                acts = [
                    Act(name="Proloque", index=0, puzzles=[
                        Puzzle(name="Getting onto the stage"),
                        Puzzle(name="Playing the anthem"),
                        Puzzle(name="Showing the slides"),
                    ]),
                    Act(name="The Call", index=10),
                    Act(name="Matryoshka", index=20),
                    Act(name="The secret meeting", index=30),
                    Act(name="Vlad", index=40)
                ]
            ),
            "Technobabylon": HelpForGame(
                acts = [
                    Act(name="Chapter 1: Prisoner of Consciousness", index=0),
                    Act(name="Chapter 10: Suicide City", index=10),
                    Act(name="Chapter 11: Fission", index=11),
                    Act(name="Chapter 100: Meeting of Minds", index=100),
                    Act(name="Chapter 101: Germination", index=101),
                    Act(name="Chapter 110: Crisis of Consciousness", index=110),
                    Act(name="Chapter 111: Jahiliyyah", index=111),
                    Act(name="Chapter 1000: Flesh Drive", index=1000),
                    Act(name="Chapter 1001: Ripper", index=1001),
                    Act(name="Chapter 1010: Runtime", index=1010),
                ]
            )
        }

    def load_help_for_game(self, game: str) -> HelpForGame:
        return self.games.get(game, None)

    def load_game_list(self) -> list[Game]:
        return self.game_list