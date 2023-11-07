from rlcard.games.mus import Dealer
from rlcard.games.mus import Player
from rlcard.games.mus import Round
from rlcard.games.mus import Card
import numpy as np

def test_pairs():
    
    dealer = Dealer(np.random.RandomState())

    players = [Player(i, np.random.RandomState()) for i in [0,1]]

    round = Round(dealer, players, np.random.RandomState())

    for player in players:
        cards = [Card(suit='O', trait='R'),
                 Card(suit='C', trait='R'),
                 Card(suit='E', trait='R'),
                 Card(suit='O', trait='2'),
                 ]
        dealer.deal_fake_cards(cards, player)

    winner = round.evaluate_pares()

    assert winner == round.lead_player

    