from collections import Counter
import numpy as np
# from rlcard.games.mus.utils import XXXX


class MusRound:

    MUS = 0
    DESCARTE = 1
    GRANDES = 2
    CHICAS = 3
    PARES = 4
    JUEGO = 5
    PUNTO = 6

    card_value = {'R': 10, '3': 10, 'C': 9, 'S': 8,
                  '7': 7, '6': 6, '5': 5, '4': 4,
                  '2': 1, '1': 1}
    
    card_value_punto = {'R': 10, '3': 10, 'C': 10, 'S': 10,
            '7': 7, '6': 6, '5': 5, '4': 4,
            '2': 1, '1': 1}


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
        self.gameplay_names = ['Mus', 'Descartes', 'Grandes', 'Chicas', 'Pares', 'Juego', 'Punto']
        self.current_gameplay = self.GRANDES # Temporarily start with GRANDES
        self.haymus = [None for _ in range(self.num_players)]
        self.state = {}
        

    def next_player(self):
        self.state["current_player"] = (self.state["current_player"] + 1) % 2

    def change_to_lead_player(self):
        self.state["current_player"] = self.state["lead_player"]

    def start_new_round(self, points):

        # Deal 4 cards to each player to prepare for the game
        for player in self.players:
            self.dealer.deal_cards(player, 4)

        assert len(self.players[0].hand) == 4
        assert len(self.players[1].hand) == 4
        
        self.state["turn"] = 0
        self.state["current_player"] = self.current_player
        self.state["current_gameplay"] = self.current_gameplay
        self.state["bids"] = [None for i in self.players]
        self.state["bet"] = [0, 0, 0, 0]
        self.state["ground_bet"] = 0
        self.state["points"] = points
        self.state["lead_player"] = self.lead_player
        self.state["current_player"] = self.lead_player
        self.state["roundover"] = False

        return self.state


    def proceed_round(self, action):

        if action not in self.get_legal_actions():
            raise ValueError("Action %s is not allowed", action)

        self.gameplay(action)

        if self.state["current_gameplay"] > self.CHICAS:
            self.evaluate()

        if self.state["current_gameplay"] == self.PARES:
            if not self.check_pairs():
                self.state["current_gameplay"] == self.JUEGO
        
        if self.state["current_gameplay"] == self.JUEGO:
            if not self.check_juego():
                self.state["current_gameplay"] == self.PUNTO

        return self.state
    
    def evaluate(self):
        winner_grandes = self.evaluate_grandes()
        self.state["roundover"] = True
        self.state["points"][winner_grandes] = self.state["points"][winner_grandes] + 1

        return None
    
    def evaluate_grandes(self):

        
        # Assumes cards are ordered
        
        for card_index in [0,1,2,3]:
            if self.card_value[self.players[0].hand[card_index].trait] > self.card_value[self.players[1].hand[card_index].trait]:
                return 0
            elif self.card_value[self.players[0].hand[card_index].trait] < self.card_value[self.players[1].hand[card_index].trait]:
                return 1
        
        return self.lead_player
    
    def evaluate_chicas(self):
        # Assumes cards are ordered
        
        for card_index in [3,2,1,0]:
            if self.card_value[self.players[0].hand[card_index].trait] < self.card_value[self.players[1].hand[card_index].trait]:
                return 0
            elif self.card_value[self.players[0].hand[card_index].trait] > self.card_value[self.players[1].hand[card_index].trait]:
                return 1
        
        return self.lead_player
    
    def evaluate_pares(self, winner=None):
        cards = []
        for idx, player in enumerate(self.players):
            cards_cnt = Counter([self.card_value_punto[player.hand[card_index].trait] for card_index in [0,1,2,3]])
            cards[idx] = cards_cnt.most_common()
            # TODO
            
        return self.lead_player
    
    def evaluate_juego(self):
      
        juego = [0, 0]
        for idx, _ in enumerate(self.players):
            juego[idx] = sum([self.card_value_juego[self.players[idx].hand[card_index].trait] for card_index in [0,1,2,3]])
            
        if juego[0] > juego[1]:
            return 0
        elif juego[0] < juego[1]:
            return 1

        return self.lead_player
    
    def evaluate_punto(self):

        punto = [0, 0]
        for idx, _ in enumerate(self.players):
            punto[idx] = sum([self.card_value_punto[self.players[idx].hand[card_index].trait] for card_index in [0,1,2,3]])

        order_punto = {31: 1, 32: 2, 40: 3, 37: 4, 36: 5, 35: 6, 34: 7, 33: 8}

        if order_punto[punto[0]] < order_punto[punto[1]]:
            return 0
        elif order_punto[punto[0]] > order_punto[punto[1]]:
            return 1

        return self.lead_player
    
    def check_pairs(self):
        pairs = 0
        for player in self.players:
            values = [self.card_value[player.hand[card_index].trait] for card_index in [0,1,2,3]]
            if len(values) != len(set(values)):
                pairs += 1
        
        if pairs == 2:
            return True
        
        return False
    
    def check_juego(self):
        juegos = 0
        for player in self.players:
            points = sum([self.card_value[player.hand[card_index].trait] for card_index in [0,1,2,3]])
            if points >= 31 and points <= 40:
                juegos += 1

        if juegos == 2:
            return True
        
        return False
    

    def mus(self, action):
        if action == "mus":
            self.haymus[self.state["current_player"]] = 1
            if self.haymus == [1, 1]:
                self.state["lance"] = 1
        elif action == "juega":
            self.state["current_gameplay"] = 0
        return None

    def descarte(self, action):
        #action here can be a list of four Booleans:
        # True to keep the card
        # False to discard
        return None
    
    def gameplay(self, action):
        other_player = (self.state["current_player"] + 1) % 2

        if action == "paso":
            self.state["bids"][self.state["current_player"]] = action
            if self.state["turn"] == 0:
                self.next_player()
                self.state["turn"] = 1
            else:
                self.next_player()
                self.state["turn"] = 0
                self.state["current_gameplay"] = self.state["current_gameplay"] + 1

        if action == "envido":
            self.state["bids"][self.state["current_player"]] = action
            self.state["ground_bet"] = self.state["ground_bet"] + 1
            self.state["lift_bet"] = 1
            self.state["turn"] = self.state["turn"] + 1
            self.next_player()

        if action == "veo":
            if self.state["bids"][other_player] == "ordago":
                self.state["current_gameplay"] = -1
            else:
                self.state["ground_bet"] = self.state["ground_bet"] + self.state["lift_bet"]
                self.state["bet"][self.state["current_gameplay"]-2] = self.state["ground_bet"]
                self.next()

        if action == "noveo":
            self.state["points"][other_player] += self.state["ground_bet"]
            self.next()

        if action == "ordago":
            self.state["bids"][self.state["current_player"]] = action
            self.state["ground_bet"] = self.state["ground_bet"] + 1
            self.next_player()
    

    def next(self):
        self.change_to_lead_player()
        self.state["bids"]= [0, 0]
        self.state["ground_bet"] = 0
        self.state["lift_bet"] = 0
        self.state["turn"] = 0
        self.state["current_gameplay"] = self.state["current_gameplay"] + 1


    def get_legal_actions(self):
        """
        Obtain the legal actions for the current player

        Returns:
           (list):  A list of legal actions
        """

        if self.state["current_gameplay"] == self.MUS:
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
