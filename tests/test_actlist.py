
from flask.testing import FlaskClient


def test_list_acts_first_act(client: FlaskClient):
    # If the user requests the acts for a game
    # and doesn't mark any acts as "solved"

    result = client.get("/v1/hints/Technobabylon/acts")

    # Then they should only see the first act

    assert "Chapter 1: Prisoner of Consciousness" in result.text
    assert "Chapter 2" not in result.text

def test_list_acts_some_act_solved(client: FlaskClient):
    # If the user requests the acts for a game
    # and has some acts marked as solved, the weasel should:
    #
    # - list all previous acts
    # - list the first unsolved act
    # - don't list any further acts

    result = client.get("/v1/hints/Technobabylon/acts?lastSolvedAct=11")

    # Then they should only see the first act

    assert "Chapter 1: Prisoner of Consciousness" in result.text
    assert "Chapter 10: Suicide City" in result.text
    assert "Chapter 11: Fission" in result.text
    assert "Chapter 100: Meeting of Minds" in result.text
    assert "Chapter 101" not in result.text