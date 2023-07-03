
from flask.testing import FlaskClient


def test_list_games(client: FlaskClient):
    response = client.get("/v1/games")

    assert "The Day of the Tentacle" in response.text
    assert "Irony Curtain: From Matryoshka with Love" in response.text
    assert "Technobabylon" in response.text