from rlcard.games.mus import Dealer
from rlcard.games.mus import Player
from rlcard.games.mus import Round
from rlcard.games.mus import Card
import numpy as np

def test_simple_round():
    np_random = np.random.RandomState()
    players = [Player(i, np_random) for i in range(2)]
    dealer = Dealer(np_random)

    round = Round(dealer, players, np_random)

    round.start_new_round([0,0])

    for idx, player in enumerate(players):
        print(f'For player number {idx+1}:')
        Card.print_cards([Card.get_str(card) for card in player.hand])

    round.proceed_round("paso")
    round.proceed_round("envido")
    round.proceed_round("envido")
    game_state = round.proceed_round("veo")

    assert game_state["roundover"] == True
