
from rlcard.games.mus.utils import init_spanish_deck
import numpy as np


class MusDealer:
    ''' Initialize a Mus dealer class
    '''
    def __init__(self, np_random):
        self.np_random = np_random
        self.deck = init_spanish_deck()
        self.deck_aside = []
        self.shuffle()

    def shuffle(self):
        ''' Shuffle the deck
        '''
        self.np_random.shuffle(self.deck)

    def use_aside_deck(self):
        ''' Convert the aside deck in the main deck
        '''

        self.deck = self.deck_aside.copy()
        self.shuffle()
        self.deck_aside = []

    def deal_cards(self, player, num):
        ''' Deal some cards from deck to one player

        Args:
            player (object): The object of DoudizhuPlayer
            num (int): The number of cards to be dealed
        '''
        for _ in range(num):
            if len(self.deck) == 0:
                self.use_aside_deck()

            player.hand.append(self.deck.pop())

    def receive_returned_cards(self, cards):
        
        if isinstance(cards, str):
            cards = [cards]

        self.deck_aside.extend(cards)
