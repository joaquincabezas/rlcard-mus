from termcolor import colored

class MusCard:

    info = {'suit': ['o', 'c', 'e', 'yb'],
            'trait': ['a', '1', '2', '3', '4', '5', '6', '7']
            }

    def __init__(self, suit, trait):
        ''' Initialize the class of MusCard

        Args:
            suit (str): The suit of card
            trait (str): The trait of card
        '''
        self.suit = suit
        self.trait = trait
        self.str = self.get_str()

    def get_str(self):
        ''' Get the string representation of card

        Return:
            (str): The string of card's color and trait
        '''
        return self.suit + '-' + self.trait


    @staticmethod
    def print_cards(cards):
        ''' Print out card in a nice form

        Args:
            card (str or list): The string form of a Spanish card or a list of stringforms of Spanish cards
        '''
        if isinstance(cards, str):
            cards = [cards]

        colors_suits = {"o": "yellow",
                  "c": "red",
                  "e": "blue",
                  "b": "green"}
        
        symbol_suits = {"o": "🥇",
            "c": "🍷",
            "e": "🗡️",
            "b": "🪵"}
        
        
        for i, card in enumerate(cards):
            suit, trait = card.split('-')

            print(colored(trait, colors_suits[suit]), end=' ')
            print(symbol_suits[suit], end='')

            if i < len(cards) - 1:
                print(', ', end='')

        print("")
