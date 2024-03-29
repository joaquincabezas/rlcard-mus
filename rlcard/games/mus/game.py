from copy import deepcopy
import numpy as np

from rlcard.games.mus import Dealer
from rlcard.games.mus import Player
from rlcard.games.mus import Round

class MusGame:

    def __init__(self, allow_step_back=False, num_players=2):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        self.num_players = num_players
        self.players = None
        self.dealer = None
        self.history = None
        self.is_over = False

    def init_game(self):
        ''' Initialize players and state

        Returns:
            (tuple): Tuple containing:

                (dict): The first state in one game
                (int): Current player's id
        '''

        # Initialize a dealer that can deal cards
        self.dealer = Dealer(self.np_random)

        # Initialize players to play the game
        self.players = [Player(i, self.np_random) for i in range(self.num_players)]

        # Initialize a Round
        
        self.round = Round(self.dealer, self.players, self.np_random)

        state = self.round.start_new_round([0, 0])

        # Save the hisory for stepping back to the last state.
        self.history = []

        player_id = state["current_player"]

        return state, player_id

    def step(self, action):
        ''' Get the next state

        Args:
            action (str): A specific action

        Returns:
            (tuple): Tuple containing:

                (dict): next player's state
                (int): next plater's id
        '''

        if self.allow_step_back:
            # First snapshot the current state
            his_dealer = deepcopy(self.dealer)
            his_round = deepcopy(self.round)
            his_players = deepcopy(self.players)
            self.history.append((his_dealer, his_players, his_round))

        state = self.round.proceed_round(action)
        player_id = state["current_player"]

        try:
            if state["is_over"] == True:
                self.is_over == True
        except:
            self.is_over == False

        return state, player_id
    

