
class MusPlayer:

    def __init__(self, player_id, np_random):
        ''' Initilize a player.

        Args:
            player_id (int): The id of the player
        '''
        self.np_random = np_random
        self.player_id = player_id
        self.hand = []
        self.chickpeas = 0
        self.mus = None

    def get_player_id(self):
        ''' Return the id of the player
        '''

        return self.player_id
    
    def return_all_cards(self):
        cards = self.hand.copy()
        self.hand = []
        return cards

    def order_cards(self):
        card_value = {'R': 10, '3': 10, 'C': 9, 'S': 8,
                '7': 7, '6': 6, '5': 5, '4': 4,
                '2': 1, '1': 1}
        
        self.hand = sorted(self.hand, key=lambda x: card_value[x.trait])
