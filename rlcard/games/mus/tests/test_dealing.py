from rlcard.games.mus.card import MusCard as Card
from rlcard.games.mus import Game

def test_deal():
    game = Game()
    game.init_game()
    cards_str = [card.get_str() for card in game.players[1].hand]
    Card.print_cards(cards_str)

if __name__ == '__main__':
    test_deal()