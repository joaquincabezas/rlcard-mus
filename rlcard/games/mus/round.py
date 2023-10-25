from rlcard.games.mus.card import UnoCard
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
        self.current_player = None
        self.num_players = num_players
        self.is_over = False
        self.winner = None
        self.lances = ['Mus', 'Grandes'] # ['Grandes', 'Chicas', 'Pares', 'Juego']
        self.lance = self.lances[0]

    def mus(self, dealer, players):
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

        if self.lance == 'mus':
            return mus_actions
        
        return game_actions