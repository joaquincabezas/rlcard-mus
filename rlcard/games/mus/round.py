import numpy as np
# from rlcard.games.mus.utils import XXXX


class MusRound:

    def __init__(self, dealer, players, np_random):
        ''' Initialize the round class

        Args:
            dealer (object): the object of UnoDealer
            num_players (int): the number of players in game
        '''
        self.np_random = np_random
        self.dealer = dealer
        self.target = None
        self.lead_player = np.random.randint(0,1)
        self.current_player = self.lead_player
        self.players = players
        self.num_players = len(self.players)
        self.is_over = False
        self.winner = None
        self.lances = ['Grandes'] # ['Mus', 'Descarte', 'Grandes', 'Chicas', 'Pares', 'Juego']
        self.lance = 0
        self.haymus = [None for _ in range(self.num_players)]
        self.state = {}
        

    def change_player(self):
        self.state["current_player"] = (self.state["current_player"] + 1) % 2

    def change_lead_player(self):
        self.state["current_player"] = self.state["lead_player"]

    def start_new_round(self, points):

        # Deal 4 cards to each player to prepare for the game
        for player in self.players:
            self.dealer.deal_cards(player, 4)
        
        self.state["turn"] = 0
        self.state["current_player"] = self.current_player
        self.state["lance"] = self.lance
        self.state["bids"] = [None for i in self.players]
        self.state["bet"] = 0
        self.state["ground_bet"] = 0
        self.state["points"] = points
        self.state["lead_player"] = self.lead_player
        self.state["current_player"] = self.lead_player
        self.state["roundover"] = False


    def proceed_round(self, action):

        if action not in self.get_legal_actions():
            raise ValueError("Action %s is not allowed", action)

        if self.state["lance"] == 0:
            self.grandes(action)
            if self.state["lance"] != 0:
                self.evaluate()
            return self.state

        self.evaluate()
        # if self.state["lance"] == 0:
        #     self.mus(action)
        # elif self.state["lance"] == 1:
        #     self.descarte(action)
        # elif self.state["lance"] == 2:
        #     self.grandes(action)
        # elif self.state["lance"] == 3:
        #     self.evaluate()

        return self.state
    
    def evaluate(self):
        winner_grandes = self.evaluate_grandes()
        self.state["roundover"] = True
        self.state["points"][winner_grandes] = self.state["points"][winner_grandes] + 1

        return None
    
    def evaluate_grandes(self):
        value = {'R': 10, '3': 10, 'C': 9, 'S': 8,
                 '7': 7, '6': 6, '5': 5, '4': 4,
                 '2': 1, '1': 1}
        
        # Assumes cards are ordered
        
        for card_index in [0,1,2,3]:
            if value[self.players[0].hand[card_index].trait] > value[self.players[1].hand[card_index].trait]:
                return 0
            elif value[self.players[0].hand[card_index].trait] < value[self.players[1].hand[card_index].trait]:
                return 1
        
        return self.lead_player

    def mus(self, action):
        if action == "mus":
            self.haymus[self.state["current_player"]] = 1
            if self.haymus == [1, 1]:
                self.state["lance"] = 1
        elif action == "juega":
            self.state["lance"] = 2
        return None

    def descarte(self, action):
        #action here can be a list of four Booleans:
        # True to keep the card
        # False to discard
        return None

    def grandes(self, action):
        other_player = (self.state["current_player"] + 1) % 2

        if action == "paso":
            self.state["bids"][self.state["current_player"]] = action
            if self.state["turn"] == 0:
                self.change_player()
                self.state["turn"] = 1
            else:
                self.change_player()
                self.state["turn"] = 0
                self.state["lance"] = self.state["lance"] + 1

        if action == "envido":
            self.state["bids"][self.state["current_player"]] = action
            self.state["ground_bet"] = self.state["ground_bet"] + 1
            self.state["bet"] = 1
            self.state["turn"] = self.state["turn"] + 1
            self.change_player()

        if action == "veo":
            if self.state["bids"][other_player] == "ordago":
                self.state["lance"] = -1
            else:
                self.state["ground_bet"] = self.state["ground_bet"] + self.state["bet"]
                self.next()

        if action == "noveo":
            self.state["points"][other_player] += self.state["ground_bet"]
            self.next()

        if action == "ordago":
            self.state["bids"][self.state["current_player"]] = action
            self.state["ground_bet"] = self.state["ground_bet"] + 1
            self.change_player()


    def next(self):
        self.change_lead_player()
        self.state["bids"]= [0, 0]
        self.state["bet"] = 0
        self.state["turn"] = 0
        self.state["lance"] = self.state["lance"] + 1


    def get_legal_actions(self):
        """
        Obtain the legal actions for the current player

        Returns:
           (list):  A list of legal actions
        """

        if self.state["lance"] == 'Mus':
            return ['mus', 'juega']
        
        if self.state["turn"] == 0:
            return ['paso', 'envido', 'ordago']
        
        other_player = (self.state["current_player"] + 1) % 2
        
        if self.state["bids"][other_player] == "paso":
            return ['paso', 'envido', 'ordago']
        elif self.state["bids"][other_player] == "envido":
            return ['envido', 'ordago', 'veo', 'noveo']
        elif self.state["bids"][other_player] == "ordago":
            return ['veo', 'noveo']
        
        return []

    
    def get_state(self):

        return self.state
