from termcolor import colored

class MusCard:

    info = {'suit': ['O', 'C', 'E', 'B'],
            'trait': ['A', '1', '2', '3', '4', '5', '6', '7']
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

        colors_suits = {"O": "yellow",
                  "C": "red",
                  "E": "blue",
                  "B": "green"}
        
        symbol_suits = {"O": "🥇",
            "C": "🍷",
            "E": "🗡️",
            "B": "🪵"}
        
        
        for i, card in enumerate(cards):
            suit, trait = card.split('-')
            suit = suit.upper()
            trait = trait.upper()

            print(colored(trait, colors_suits[suit]), end=' ')
            print(symbol_suits[suit], end='')

            if i < len(cards) - 1:
                print(', ', end='')

        print("")
