from rlcard.games.mus import Dealer
from rlcard.games.mus import Player
import numpy as np

def test_deck():
    anon_player = Player(1, np.random.RandomState())
    deck = Dealer(np.random.RandomState())
    try:
        deck.deal_cards(anon_player,1)
    except:
        assert False, "error dealing cards"

def test_aside_deck():
    anon_player = Player(1, np.random.RandomState())
    deck = Dealer(np.random.RandomState())
    deck.deal_cards(anon_player,30)
    deck.receive_returned_cards(anon_player.return_all_cards())
    try:
        deck.deal_cards(anon_player,30)
    except:
        assert False, "aside deck not working"

if __name__ == "__main__":
    test_aside_deck()



