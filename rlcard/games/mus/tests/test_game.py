from rlcard.games.mus import Game
from rlcard.games.mus import Round

def test_simplegame():
    mus = Game()

    game_state, player_id = mus.init_game()

    assert player_id == 0

    mus.step("paso")
    mus.step("envido")
    game_state, player_id = mus.step("veo")

    assert game_state["current_gameplay"] == Round.CHICAS

    mus.step("paso")
    game_state, player_id = mus.step("paso")

    assert game_state["current_gameplay"] == Round.PARES
    assert game_state["roundover"] == True