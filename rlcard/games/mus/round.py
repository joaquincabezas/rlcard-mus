from rlcard.games.mus.card import UnoCard
import numpy as np
# from rlcard.games.mus.utils import XXXX


class MusRound:

    def __init__(self, state, dealer, players, np_random):
        ''' Initialize the round class

        Args:
            dealer (object): the object of UnoDealer
            num_players (int): the number of players in game
        '''
        self.np_random = np_random
        self.dealer = dealer
        self.target = None
        self.current_player = np.random.randint(0,1)
        self.players = players
        self.is_over = False
        self.winner = None
        self.lances = ['Grandes'] # ['Mus', 'Descarte', 'Grandes', 'Chicas', 'Pares', 'Juego']
        self.lance = 0
        self.haymus = [None for _ in range(self.num_players)]
        self.state = state

    def change_player(self):
        self.current_player = (self.current_player + 1) % 1

    def start_new_round(self):

        # Deal 4 cards to each player to prepare for the game
        for player in self.players:
            self.dealer.deal_cards(player, 4)
        
        self.state["turn"] = 0
        self.state["current_player"] = self.current_player
        self.state["lance"] = self.lance
        self.state["bids"] = ["" for i in self.players]


    def proceed_round(self, players, action):


        if self.lance == 0:
            self.grandes(action)
        else:
            self.evaluate()
        # if self.lance == 0:
        #     self.mus(action)
        # elif self.lance == 1:
        #     self.descarte(action)
        # elif self.lance == 2:
        #     self.grandes(action)
        # elif self.lance == 3:
        #     self.evaluate()
    
    def evaluate(self):
        grandes_player, grandes_points = self.evaluate_grandes()

        return None
    
    def evaluate_grandes(self):
        player = 0
        points = 0

        return player, points

    def mus(self, action):
        if action == "mus":
            self.haymus[self.current_player] = 1
            if self.haymus == [1, 1]:
                self.lance = 1
        elif action == "juega":
            self.lance = 2
        return None

    def descarte(self, action):
        #action here can be a list of four Booleans:
        # True to keep the card
        # False to discard
        return None

    def grandes(self, action):
        if action == "paso":
            self.state["bids"][self.current_player] = action
            next()
        elif action == "envido":
            self.state["bids"][self.current_player] = action
            self.next()


    def next(self):
        if self.state["turn"] == 0:
            self.change_player()
            self.state["turn"] = 1
        else:
            self.change_player()
            self.state["turn"] = 0
            self.lance = self.lance + 1
        

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
    
    def get_state(self):

        return self.state
