from rlcard.games.mus.card import UnoCard
import numpy as np
# from rlcard.games.mus.utils import XXXX


class MusRound:

    def __init__(self, dealer, num_players, np_random):
        ''' Initialize the round class

        Args:
            dealer (object): the object of UnoDealer
            num_players (int): the number of players in game
        '''
        self.np_random = np_random
        self.dealer = dealer
        self.target = None
        self.current_player = np.random.randint(0,1)
        self.num_players = num_players
        self.is_over = False
        self.winner = None
        self.lances = ['Mus', 'Descarte', 'Grandes'] # ['Chicas', 'Pares', 'Juego']
        self.lance = self.lances[0]
        self.haymus = [None for _ in range(self.num_players)]

    def change_player(self):
        self.current_player = (self.current_player + 1) % 1

    def proceed_round(self, players, action):

        if self.lance == "Mus":
            self.mus(players, action)
        elif self.lance == "Descarte":
            self.descarte(players, action)
        elif self.lance == "Grandes":
            self.grandes(players, action)

    def mus(self, players, action):
        if action == "mus":
            self.haymus[self.current_player] = 1
            if self.haymus == [1, 1]:
                self.lance = "Descarte"
        elif action == "juega":
            self.lance = "Grandes"
        return None

    def descarte(self, players, action):
        return None

    def grandes(self, dealer, players):
        return None
    
    def get_legal_actions(self):
        """
        Obtain the legal actions for the current player

        Returns:
           (list):  A list of legal actions
        """
        mus_actions = ['mus', 'juega']
        game_actions = ['paso', 'envido', 'ordago', 'veo', 'noveo']

        if self.lance == 'Mus':
            return mus_actions
        
        return game_actions